from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from blog.forms import *
from blog.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView

@login_required 
def home(request):
    return render(request, "blog/home.html")

@login_required 
def about(request):
    return render(request, "blog/about.html")

@login_required 
def writeReview(request):
    return render(request, "blog/writeReview.html")

@login_required 
def writeReview(request):
    if request.method == 'POST':
        miForm = FormNewReview(request.POST, request.FILES)
        print(miForm)
        if miForm.is_valid:
            instance = miForm.save(commit=False)
            instance.author = request.user
            instance.save()
            return render(request, "blog/home.html")
    else:
        miForm = FormNewReview()
        return render(request, "blog/writeReview.html", {"miForm":miForm})

@login_required 
def reviewList(request):
    reviews = review.objects.all()
    return render(request, "blog/reviewList.html",{"reviews": reviews})

@login_required 
def getReview(request, titulo_review):
    Review = review.objects.get(titulo= titulo_review)
    return render(request, "blog/review.html",{"Review": Review})

class CustomLogoutView(LogoutView):
    next_page='login'

@login_required 
def eliminarReview(request, TituloReview):
    Review = review.objects.get(titulo= TituloReview)
    Review.delete()
    reviews = review.objects.all()
    return render(request, "blog/reviewList.html",{"reviews": reviews})


def loginWeb(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
    return render(request, 'blog/profile/login.html', {'error': 'Usuario o contraseña incorrectos'})

def register(request):
    if request.method == "POST":
        userCreate = UserRegistrationForm(request.POST)
        if userCreate.is_valid():
            userCreate.save()
            return redirect('login')
        else:
            return render(request, 'blog/profile/register.html', {'form': userCreate})
    else:
        userCreate = UserRegistrationForm()
    return render(request, 'blog/profile/register.html', {'form': userCreate})

@login_required  
def profileview(request):
    usuario = request.user
    Info,  created =extraInfo.objects.get_or_create(user= usuario)
    return render(request, 'blog/profile/profile.html', {"Info": Info})
    
    #return render(request, 'blog/profile/profile.html')

@login_required
def editProfile(request):
    usuario = request.user
    user_basic_info = User.objects.get(id=usuario.id)
    datosExtra, created = extraInfo.objects.get_or_create(user=usuario)

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            datosExtra.description = form.cleaned_data.get('description')
            datosExtra.link = form.cleaned_data.get('link')
            user_basic_info.save()
            datosExtra.save()
            return render(request, 'blog/profile/profile.html')
    else:
        form = UserEditForm(
            initial={'username': usuario.username, 'email': usuario.email})
        return render(request, 'blog/profile/editprofile.html', {"form": form})

@login_required    
def editReview(request, TituloReview):
    Review = review.objects.get(titulo= TituloReview)
    if request.method == 'POST':
        miForm = FormNewReview(request.POST, request.FILES)
        if miForm.is_valid:
            print(miForm)
            data = miForm.cleaned_data

            Review.titulo = data['titulo']
            Review.album = data['album']
            Review.review = data['review']
            Review.score = data['score']
            Review.albumCover = data['albumCover']
            Review.save()
            reviews = review.objects.all()
            return render(request, "blog/reviewList.html", {"reviews": reviews})
    else:
        miForm = FormNewReview(initial={'titulo': Review.titulo, 'album': Review.album, 'review': Review.review, 'score':Review.score,'albumCover':Review.albumCover})
    return render(request, "blog/editReview.html", {"miForm":miForm})

@login_required
def changePassword(request):
    usuario = request.user    
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse("Las constraseñas no coinciden")
        return render(request, "blog/home.html")
    else:
        form = ChangePasswordForm(user = usuario)
        return render(request, 'blog/profile/changePassword.html', {"form": form})
    
def add_comment_to_post(request, pk):
    post = get_object_or_404(review, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
# Create your views here.
