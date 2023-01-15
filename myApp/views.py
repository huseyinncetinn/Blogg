from django.shortcuts import render , redirect 
from .models import *
from django.http import HttpResponseRedirect
from .forms import YorumForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .forms import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate
from django.db.models import Q





# Create your views here.

def search(request):
     
    kullanicilar = ''
    searched = ''
    if request.GET.get('searched'):
        searched = request.GET['searched']
        kullanicilar = Profile.objects.filter(
            name__contains = searched
        ) 

    content = {
       
       'kullanicilar' : kullanicilar
     
    }
    return render(request , 'search.html' , content)

def index(request):
    return render (request , 'index.html')

def hakkimda(request):
    return render (request , 'hakkimda.html')

def blogs(request):
    posts= Post.objects.all()
    context = {
        'posts' : posts 
    }
    return render ( request , 'blogs.html' ,context)

def blogs_detay(request,postId):
    postdetay = get_object_or_404(Post , slug = postId)
    
    profil = postdetay.olusturan.profile
    print(profil)

    form = YorumForm(request.POST or None)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'begen' in request.POST:
                if Post.objects.filter(like__in = [request.user], slug = postId).exists():
                    yazi = Post.objects.get(slug = postId)
                    yazi.like.remove(request.user)
                    yazi.save()
                    return redirect ('blogdetay' , postId = postId)
                else:
                    yazi = Post.objects.get(slug = postId)
                    yazi.like.add(request.user)
                    yazi.dislike.remove(request.user)
                    yazi.save()
                    return redirect ('blogdetay' , postId = postId)
          

            if 'begenme' in request.POST:
                if Post.objects.filter(dislike__in = [request.user], slug = postId).exists():
                    yazi = Post.objects.get(slug = postId)
                    yazi.dislike.remove(request.user)
                    yazi.save()
                    return redirect ('blogdetay' , postId = postId)

                else:
                    yazi = Post.objects.get(slug = postId)
                    yazi.dislike.add(request.user)
                    yazi.like.remove(request.user)
                    yazi.save()
                    return redirect ('blogdetay' , postId = postId)

            if 'paylas' in request.POST:
                if Post.objects.filter(retweet__in = [request.user], slug = postId).exists():
                    yazi = Post.objects.get(slug = postId)
                    yazi.retweet.remove(request.user)
                    return redirect ('blogdetay' , postId = postId)

                else:
                    yazi = Post.objects.get(slug = postId)
                    yazi.retweet.add(request.user)   
                    return redirect ('blogdetay' , postId = postId)

                   
    if form.is_valid():
        yorum = form.save(commit=False)
        yorum.post = postdetay
        yorum.kullanici = request.user
        yorum.save()
    yorumlar = Yorum.objects.filter(post = postdetay)
    context= {
        'postdetay' : postdetay , 
        'form' : form,
        'yorum' : yorumlar,
        'profil':profil
        
    }
    
    return render (request , 'blog-detay.html' ,context)
 
def createPost (request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
           form = form.save(commit=False)
           form.olusturan = request.user
           form.save()
           messages.success(request , 'Post Oluşturuldu')
           return redirect('blogs')
    context = {
        'form' : form
    }       
    return render (request , 'create.html' , context)

def createProfil(request):
    form = ProfilForm
    if request.method == 'POST':
        form = ProfilForm(request.POST , request.FILES)
        if form.is_valid():
            form.kullanici = request.user
            form.save()
            messages.success(request , 'Profil Oluşturuldu')
            return ('index')
    context ={
        'form' : form
    }        
    return render (request , 'createprofil.html' , context)

def deletePost(request , id):
    user = request.user.profile

    post = get_object_or_404(Post , id=id)
    post.delete()
    return redirect('profil' , slug = user.slug , pk = user.id)

def profil (request , slug, pk):
    profile = Profile.objects.filter(slug = slug).get(pk=pk)
    kullanici = profile.kullanici
    posts = Post.objects.filter(olusturan = kullanici ).order_by('-tarih')
    begenilenler = Post.objects.filter(like__in = [kullanici]).order_by('-tarih') 
    retweetler = Post.objects.filter(retweet__in = [kullanici]).order_by('-tarih')
    if request.user.is_authenticated:
        hesabim = Profile.objects.get(kullanici = request.user)
        if 'takip' in request.POST:
            profile.followers.add(request.user)
            profile.save()
            hesabim.follow.add(profile)
            return redirect('profil', slug = profile.slug, pk = profile.id)
            
        if 'cik' in request.POST:
            profile.followers.remove(request.user)
            hesabim.follow.remove(profile)
            profile.save()

            return redirect('profil', slug = profile.slug, pk = profile.id)

    
    print(hesabim)
    print(profile)

        

        

    
         
    followers = profile.followers.all()
    follow = profile.follow.all()

   

    if len(followers) == 0 :
        is_following = False

    for follower in followers:
        if follower == request.user:
            is_following =True
            break
        else:
            is_following =False


    

    
    

    context = {
        'kullanici' : kullanici,
        'profile' : profile,
        'posts' : posts,
        
        'is_following' : is_following,
        'begenilenler' :begenilenler,
        'retweetler' : retweetler,
        'followers':followers,
        'follow':follow
    }
    return render (request , 'profile.html' , context)

def editProfil (request):
    user = request.user.profile
    profilDuzenle = ChangeProfil(instance = user)

    if request.method == 'POST':
        profilDuzenle = ChangeProfil(request.POST , request.FILES , instance = user)
        if profilDuzenle.is_valid():
           profilDuzenle.save()
           return redirect('profil' , slug = user.slug, pk = user.id)
          
    context = {
        'profilDuzenle' :profilDuzenle
    }

    return render (request , 'editprofil.html', context)

def sifre(request):
    user = request.user

    if request.method == 'POST':
        eski = request.POST['eski']
        yeni1 = request.POST['yeni1']
        yeni2 = request.POST['yeni2']

        yeni = authenticate(request , username = user , password = eski)

        if yeni is not None :
            if yeni1 == yeni2 :
                user.set_password(yeni1)
                user.save()
                messages.success(request, 'Şifreniz Değiştirildi')
                return redirect('login')

            else:
                messages.error(request , 'Şifreler uyuşmuyor')
                return redirect('sifre')
        else:
            messages.error(request , 'Eski şifreniz hatalı')
            return redirect ('sifre')
    return render (request , 'sifre.html')                

def takipci (request,pk):
    # takip = User.objects.get(id=pk)
    profil = Profile.objects.get(id = pk)
    followers = profil.followers.all()
    for i in followers:
        print(i.profile.name)
    print(profil)
    context = {
      'takipciler' :followers
     }
    return render (request , 'takipci.html' , context)
 


def takip (request,pk):
    # takip = User.objects.get(id=pk)
    profil = Profile.objects.get(id = pk)
    follow = profil.follow.all()
    for i in follow:
        print(i.slug)
    context = {
      'takipciler' :follow
     }
    return render (request , 'takip.html' , context)
 