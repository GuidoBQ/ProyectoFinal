from django.shortcuts import render
from blog.forms import *
from blog.models import *

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
            Review = review(titulo=data["titulo"],album=data["album"], review = data["review"], albumCover = data["albumCover"])
            Review.save()
            return render(request, "blog/home.html")
    else:
        miForm = FormNewReview()
        return render(request, "blog/writeReview.html", {"miForm":miForm})

# Create your views here.
