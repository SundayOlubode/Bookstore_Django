from django.db import models

# Create your models here.
class Author(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=15)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    dob = models.DateField(verbose_name="Date of Birth")
    bio = models.TextField(max_length=300)

    def is_valid_password(self, raw_password):
        if self.password != raw_password:
            return False
        return True


class Book(models.Model):
    title = models.CharField(max_length=30, unique_for_date="released_year")
    released_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)