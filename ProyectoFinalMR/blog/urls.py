from django.contrib import admin
from django.urls import path, include
from blog.views import *

urlpatterns = [
    path('', home),
    path('home/', home, name="Home"),
    path('about/', about, name="About"),
    path('writeReview/', writeReview, name="WriteReview"),
    path('reviewList', reviewList, name="ReviewList")
]