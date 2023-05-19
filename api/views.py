from rest_framework.response import Response
from rest_framework.decorators import api_view

from database.backend import AuthorBackend

from database.models import Author, Book
from .serializer import AuthorSerializer, BookSerializer

# Create your views here.
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Please provide login details'}, status=401)
    
    existing_author = Author.objects.filter(email=email).exists()

    if not existing_author:
        return Response({'error': 'Author not found. Please register'}, status=401)
    
    valid_password = AuthorBackend.authenticate(Response, email, password)

    if not valid_password:
        return Response({'error': 'Email or Password Incorrect!'}, status=400)
    
    author = Author.objects.get(email=email)

    serialized = AuthorSerializer(author)
    author_data = serialized.data

    custom_login(request, author_data)
    
    return Response({'success': 'Login successful!', "data": author_data}, status=200)


@api_view(['GET'])
def getBooks(request):
    Books = Book.objects.all()
    serialized = BookSerializer(Books, many=True)

    return Response(status=200, data=serialized.data)

@api_view(['POST'])
def postBook(request):
    book_payload = request.data

    author_id = request.session.get('author_id')

    book_payload['author'] = author_id

    serializer = BookSerializer(data=book_payload)

    if not serializer.is_valid():
        return Response(status=400, data='Please input valid book data')
    
    serializer.save()
    return Response(status=201, data='Book added successfully!')

@api_view(['GET'])
def getAuthors(request):
    Authors = Author.objects.all()
    serialized = AuthorSerializer(Authors, many=True)

    return Response(status=200, data=serialized.data)

@api_view(['POST'])
def register(request):
    serializer = AuthorSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=400, data='Please input valid data')
    serializer.save()
    return Response(status=201, data='Author registered successfully!')

def custom_login(request, author):
    request.session['author_id'] = author['id']
    request.session['author_email'] = author['email']
    request.session.modified = True
    return