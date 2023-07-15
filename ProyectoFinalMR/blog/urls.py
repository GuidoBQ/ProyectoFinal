from django.contrib import admin
from django.urls import path, include
from blog.views import *

urlpatterns = [
    path('', loginWeb, name="login"),
    path('home/', home, name="Home"),
    path('about/', about, name="About"),
    path('writeReview/', writeReview, name="WriteReview"),
    path('reviewList', reviewList, name="ReviewList"),
    path('review/<titulo_review>', getReview, name="Review"),
    path('Logout/',CustomLogoutView.as_view(), name="Logout"),
    path('register/', register, name="Register"),
]