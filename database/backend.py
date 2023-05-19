from django.contrib.auth.backends import BaseBackend
from .models import Author

class AuthorBackend(BaseBackend):
    def authenticate(Response, email=None, password=None):
        try:
            author = Author.objects.get(email=email)
            return author.is_valid_password(password)
        except:
            return Response({'error': 'Password Validation Failed!'})

    def get_user(self, user_id):
        try:
            return Author.objects.get(pk=user_id)
        except Author.DoesNotExist:
            return None
