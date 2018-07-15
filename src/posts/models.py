from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

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
    publication_date = models.DateTimeField()
    image = models.URLField(blank=True)
    video = models.URLField(blank=True)
    price = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True) # set date when object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated

    category = models.ManyToManyField(Category)


    def __str__(self):
        """
        Devuelve la representación de un objeto como una string
        """
        return self.title

    def clean(self):
        # Don't allow empty image or video.
        if (self.image == '' or self.image == None) and (self.video == '' or self.video == None):
            raise ValidationError(_('You must set and image or video.'))

