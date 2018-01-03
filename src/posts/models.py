from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Devuelve la representación de un objeto como una string
        """
        return self.name

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    summary = models.TextField()
    body = models.TextField()
    director_name = models.CharField(max_length=100)
    publication_date = models.DateField()
    image = models.URLField()
    video = models.URLField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True) # set date when object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated

    # relacionando con las categorias
    # comportamientos
    # CASCADE -> Cascade deletes. Django emulates the behavior of the SQL constraint ON DELETE CASCADE and also deletes the object containing the ForeignKey.
    # PROTECT -> Prevent deletion of the referenced object by raising ProtectedError, a subclass of django.db.IntegrityError.
    category = models.ManyToManyField(Category)

    def __str__(self):
        """
        Devuelve la representación de un objeto como una string
        """
        return self.title