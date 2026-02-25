from django.shortcuts import render
from .forms import RegistrationForm
from .forms import LoginForm
from django.http import HttpResponseRedirect
from .models import ShopUser




def registration(request):
    
    
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        
        if(request.POST.get('password') == request.POST.get('password1')): 
            if not get_user(request,request.POST.get('login')):
                form.save()
            else:
                error = 'Ползователь с таким ником уже существует'
                
            if(login(request)):
                save_login(request)
                return HttpResponseRedirect('/') 
            
        
        
    form = RegistrationForm()
    
    return render(request, 'authorisation/reg.html',{'form':form, 'error':error})
def save_login(request):
    request.session['login'] = request.POST.get('login')
    request.session['password'] = request.POST.get('password')
    request.session.set_expiry(3600)
    return 

def login_page(request):
    form = LoginForm()
    error = ''
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        _login = request.POST.get('login')
        _password = request.POST.get('password')
        try:
            user = ShopUser.objects.get(login=_login)
            if(login(request,_login,_password)):
                save_login(request)
                return HttpResponseRedirect('/')
            else:
                error = 'Неправильный логин или пароль'
        except ShopUser.DoesNotExist:
            error = 'Такого пользователя не существует'
            
        except ShopUser.MultipleObjectsReturned: 
            return HttpResponseRedirect('/registration/')
        
        
    return render(request, 'authorisation/login.html', {'error':error, 'form': form})
def login(request, logIn:str = '',passWord:str = ''):
    print(logIn,passWord)
    _login:str = ''
    _password:str = ''
    if(not(logIn != '' or passWord != '')):
        
        _login = request.session.get('login')
        _password = request.session.get('password')
    else:
        _login = logIn
        _password = passWord
    user = get_user(request,_login)
    if(_login != '' or _password != ''):
        if(user and user.password == _password):
            return True
        else: 
            
            return False
    else:
        
        return False
def get_user(request, logIn:str = ''):
    _login:str = ''
    if logIn == '':
        _login = request.session.get('login')
    else:
        _login = logIn
    if(_login == ''):
        return None
    try:
        
        return ShopUser.objects.get(login=_login)
    except ShopUser.DoesNotExist:
        
        return None
    except ShopUser.MultipleObjectsReturned:
        
        return None
    
def logout(request):
    
    request.session.flush()
    return HttpResponseRedirect('/')