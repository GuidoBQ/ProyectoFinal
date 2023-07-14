from django.contrib import admin
from django.urls import path, include
from blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', loginWeb),
    path('home/', home, name="Home"),
    path('about/', about, name="About"),
    path('writeReview/', writeReview, name="WriteReview"),
    path('reviewList', reviewList, name="ReviewList"),
    path('review/<titulo_review>', getReview, name="Review"),
    path('login/', loginWeb, name="login"),
    path('Logout/',LogoutView.as_view(template_name = 'blog/profile/login.html'), name="Logout"),
    path('register/', register, name="Register"),
]