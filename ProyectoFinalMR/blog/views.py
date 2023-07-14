from django.shortcuts import render
from blog.forms import *
from blog.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")

def writeReview(request):
    return render(request, "blog/writeReview.html")

def writeReview(request):
    if request.method == 'POST':
        miForm = FormNewReview(request.POST)
        print(miForm)
        if miForm.is_valid:
            data = miForm.cleaned_data
            Review = review(titulo=data["titulo"],album=data["album"], review = data["review"],score=data["score"], albumCover = data["albumCover"])
            Review.save()
            return render(request, "blog/home.html")
    else:
        miForm = FormNewReview()
        return render(request, "blog/writeReview.html", {"miForm":miForm})

def reviewList(request):
    reviews = review.objects.all()
    return render(request, "blog/reviewList.html",{"reviews": reviews})

def getReview(request, titulo_review):
    Review = review.objects.get(titulo= titulo_review)
    return render(request, "blog/review.html",{"Review": Review})

def loginWeb(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, 'blog/home.html')
        else:
            return render(request, 'blog/profile/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'blog/profile/login.html')

def register(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return render(request, 'blog/profile/login.html')
    else:
        return render(request, 'blog/profile/register.html')

# Create your views here.
