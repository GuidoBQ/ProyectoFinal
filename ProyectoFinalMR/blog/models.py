from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings

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
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )



class extraInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description= models.TextField(null=True, blank=True)
    link= models.URLField(max_length=200, default="Sin Links")


class Comment(models.Model):
    post = models.ForeignKey('blog.review', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    text = models.TextField()
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #SubCarpeta de avatares
    image = models.ImageField(upload_to='img/', null = True, blank = True)
# Create your models here.
