from django.db import models

class review(models.Model):
    titulo = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    review = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    albumCover =  models.ImageField(null=True, blank=True, upload_to="img/")
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

# Create your models here.
