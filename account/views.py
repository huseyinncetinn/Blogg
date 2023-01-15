from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User
from myApp.models import *
# Create your views here.

def login_request(request):
    if request.method == 'POST':  # eğer formdaki bilgiler POST edilmişse
        username = request.POST['username']  # inputtaki değerleri çekiyoruz ki server tarafında karşılaştırma yapalım var mı yok mu 
        password = request.POST['password']
        print(request.POST)
        print(password)

        user =authenticate(request , username = username ,  password = password ) #birinci serverdaki bilgi ikincisi kullanıcıdan alınan bilgi

        if user is not None: # eğer kullanıcı serverda yok değilse yani varsa
            login(request , user)
            redirect('index')
        else:
            return render (request , 'account/login.html',
             {
                'error' : 'username or password incorrect'
             }
            )     
     

    return render (request , 'account/login.html')


def register_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        repassword = request.POST['repassword']
        bio = request.POST['bio']
        

        if password == repassword :
           if User.objects.filter(username = username).exists(): # exists bize var mı yok mu diye true ya da false değer verir
               return render (request , 'account/register.html', {
                'error' : 'Bu username başka kullanıcı tarafından kullanılıyor',
                'username' : username ,
                'email' : email , 
                'firstname' : firstname ,
                'lastname' : lastname
                }) 
           else :
                if User.objects.filter(email = email).exists():   
                   return render (request , 'account/register.html', {
                    'error' : 'Bu email zaten kullanılıyor',
                    'username' : username ,
                    'email' : email , 
                    'firstname' : firstname ,
                    'lastname' : lastname
                    }) 
                else:
                    user = User.objects.create_user(username = username , email = email , first_name =firstname , last_name = lastname , password = password)
                    # ilk kısım User objesinden dönen değer diğeri bizim değişkenimiz
                    Profile.objects.create(
                        kullanici = user,
                        name = firstname,   
                        bio = bio,
                        
                    )
                    user.save()
                    return redirect('login')
        else:
            return render (request , 'account/register.html', {
                'error' : 'Parolar eşleşmiyor',
                'username' : username ,
                'email' : email , 
                'firstname' : firstname ,
                'lastname' : lastname
                })      


    return render (request , 'account/register.html')


def logout_request(request):
    logout(request)
    return redirect ('index')        
