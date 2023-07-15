from django.db import models
from django.contrib.auth.models import User

class review(models.Model):
    scorePick = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        )
    titulo = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    review = models.TextField(null=True, blank=True)
    score = models.CharField(max_length=10, choices=scorePick, default='uno')
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    albumCover =  models.ImageField(null=True, blank=True, upload_to="img/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

# Create your models here.
