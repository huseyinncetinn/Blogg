from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index ,name='index'),
    path('hakkimda/' , views.hakkimda , name='hakkimda' ),
    path('blogs/' , views.blogs , name='blogs'),
    path('blogdetay/<slug:postId>' , views.blogs_detay , name='blogdetay'),
    path('create/' , views.createPost , name='create'),
    path('profile/<str:slug>/<int:pk>' , views.profil , name='profil'),
    path('editProfil/' , views.editProfil , name='editProfil'),
    path('deletePost/<int:id>' , views.deletePost , name='deletePost'),
    path('sifre/' , views.sifre , name='sifre'),
    path('search/' , views.search , name='search'),
    path('takipci/<int:pk>' , views.takipci , name='takipci'),
    path('takip/<int:pk>', views.takip, name='takip')
  
]
