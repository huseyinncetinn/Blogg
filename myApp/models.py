from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    olusturan = models.ForeignKey(User , on_delete=models.CASCADE ,null = True)
    baslik = models.CharField(max_length=50)
    kisaBilgi = models.CharField(max_length=100)
    resim = models.FileField(upload_to= 'posts/')
    tarih = models.DateTimeField(auto_now_add= True)
    icerik = RichTextField(max_length= 10000)
    slug = models.SlugField(null=True , unique= True , blank=True , editable=False)
    retweet = models.ManyToManyField(User,related_name='retweet')
    like = models.ManyToManyField(User, related_name='like')
    dislike = models.ManyToManyField(User, related_name='dislike')
    def __str__(self):
        return self.baslik


    def save(self , *args , **kwargs):
        self.slug = slugify(self.baslik)
        super().save(*args , **kwargs)


class Profile(models.Model):
    kullanici = models.OneToOneField(User , null=True , on_delete = models.CASCADE)
    name = models.CharField(max_length=30 , blank= True , null=True )
    profil_resim = models.ImageField(null=True , blank=True ,upload_to='posts/profil_resim/' , default='posts/profil_resim/default.jpg' )
    bio = models.TextField()
    slug = models.SlugField(null=True , unique= True , blank=True , editable=False)
    followers = models.ManyToManyField(User , blank=True , related_name='followers')
    follow = models.ManyToManyField('self', related_name='follow', blank=True)
    def save(self , *args , **kwargs):
        self.slug = slugify(self.kullanici)
        super().save(*args , **kwargs)

    def __str__(self):  
        return str(self.kullanici) 

class Yorum(models.Model):
    post = models.ForeignKey( Post , related_name='yorum' , on_delete=models.CASCADE)
    yorum = RichTextField(max_length= 10000)
    yorumTarih = models.DateTimeField(auto_now_add=True)
    kullanici = models.ForeignKey(User , null=True , on_delete = models.CASCADE)
    

    def __str__(self):
        return self.post.baslik



    

class Hesap(models.Model):
    isim = models.CharField(max_length=100)
    takipci = models.ManyToManyField('self', blank=True)
    
    def __str__(self):
        return self.isim

