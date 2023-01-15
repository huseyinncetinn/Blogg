from django import forms 
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm



class YorumForm (forms.ModelForm):
    class Meta:
        model = Yorum
        fields = [
            # 'kullanici',
            'yorum',
        ]
    def __init__(self , *args , **kwargs):
        super(YorumForm , self).__init__(*args ,**kwargs)
        for kullanici , field in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})     

class PostForm (ModelForm):
    class Meta:
        model = Post
        fields = [
            
            'baslik' , 
            'kisaBilgi' ,
            'resim' ,
            'icerik']
    def __init__(self , *args , **kwargs):
        super(PostForm , self).__init__(*args , ** kwargs)
        for name ,field in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})

class ProfilForm (ModelForm):
    class Meta :
        model = Profile
        fields = [
            'name' , 'profil_resim' , 'bio'
        ]
    def __init__(self, *args , **kwargs):
        super(ProfilForm , self).__init__(*args , **kwargs)
        for name , field in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})



class ChangeProfil (ModelForm):
    class Meta:
        model = Profile
        fields =  [
           'name' , 'profil_resim' , 'bio'
        ]   
    def __init__(self , *args , **kwargs):
        super(ChangeProfil , self).__init__(*args , **kwargs)
        for name , field in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})    

# class EditUserProfileForm(UserChangeForm):

#     name = forms.CharField(  max_length=50 , widget=forms.TextInput(attrs={'class' : 'form-control'}))
#     profil_resim = forms.ImageField(widget=forms.FileInput(attrs={'class' : 'form-control'}))
#     bio = forms.CharField ( max_length=150, widget=forms.TextInput(attrs={'class' : 'form-control'}))

#     class Meta:
#         model : Profile
#         fields = [
#             'name' , 'profil_resim' , 'bio'
#          ]

