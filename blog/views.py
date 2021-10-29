from django.shortcuts import redirect, render
from .models import Post,Profile, Post, Like
from .forms import PostForm, ProfileForm, RegisterForm, LikeForm
from django.contrib import messages 

from django.contrib.auth.models import User 
from  django.views import View

# Create your views here.

def home(request):
    posts = Post.objects.all()
    
    context={
        'posts':posts,
    }
    return render(request, 'home.html', context)



def about(request):
    return render(request, 'about.html')




def register(request):
    if request.method == 'POST':
        
       form = RegisterForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, f'Your account has been created. You can log in now!')
           return redirect('login')
    
    else :
        form= RegisterForm()
      
    context ={'form':form}  
             
    return render(request, 'register.html',context)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = Post.objects.filter(user = request.user.id)
    try:
        profile = Profile.objects.get(user = request.user)
    
    except Profile.DoesNotExist:
        profile= None
        
    context = {
        'posts' : posts,
        'profile' : profile
    }
    return render(request, 'profile.html',context)

def profileadd(request): 

    if not request.user.is_authenticated:
        return redirect('login')    

    form = ProfileForm()

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)

        #id burada yüklenir
        obj = form.save(commit=False) # Return an object without saving to the DB
        obj.user = User.objects.get(pk=request.user.id)

        if form.is_valid():
            
            form.save() 
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'profileadd.html', context)

def profileupdate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = Profile.objects.get(user = request.user.id)
    form = ProfileForm(instance=user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('profile')
    
    context = {
        "form" : form,
    }
    
    return render(request, 'profileupdate.html', context)


def addpost(request): 
    if not request.user.is_authenticated:
        return redirect('login')

    form = PostForm()

    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)
        ## id aldıracak
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=request.user.id)
        
        if(form.is_valid()):
            form.save()
            return redirect('profile')
            
    context = {
        'form': form,
    }
    return render(request, 'addpost.html', context)


def updatepost(request, id): 
    if not request.user.is_authenticated:
        return redirect('login')
    
    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)
     
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'updatepost.html', context)


def deletepost(request, id): 
    if not request.user.is_authenticated:
        return redirect('login')
    
    post =  Post.objects.get(pk=id)
    form = PostForm(instance=post)
    
    if request.method == 'POST':
        post.delet()
        return redirect('profile')
    
    context = {
        'form': form,
    }

    return render(request, 'deletepost.html', context)

def like(request,id):
   if request.user.is_authenticated:
       
       user = User.objectsget(id=request.user.id)
       post =  Post.objects.get(id=id)
       b1 = Like(user=user, post=post)
       
       instance = Like.objects.filter(user=b1.user, post=b1.post)
       if instance:
                instance.delete()
       else:
        b1.save()
         
    
        return redirect('home')
       
       

def postdetail(request, slug):
    
    post = Post.objects.get(slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'postdetail.html', context)