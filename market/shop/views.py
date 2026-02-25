from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from registration import views as reg_views
from products.models import Product
import array


# Create your views here.
def index(request):
    auth:bool
    items = Product.objects.all()
    if reg_views.login(request):
        auth = True
    else:
        auth = False
    return render(request,'shop/index.html', {'auth': auth, 'items':items})  
def cards(request):
    items = []
    user = reg_views.get_user(request)
    for i in user.user_products:
        try:
            prod = Product.objects.get(id = i)
            items.append(prod)
        except Product.DoesNotExist:
            continue

    if(reg_views.login(request)):
        pass
    else:
        return HttpResponseRedirect('/login/')
   
    return render(request,'shop/cards.html', {'items':items}) 
    
def action_click(request):
    if(reg_views.login(request)):
        _login = request.session.get('login')
        if request.method == 'POST':
            item_id = request.POST.get('item_id')
            action = request.POST.get('action')

            
            try:
                user = reg_views.get_user(request,_login)
                if not(user): return HttpResponseRedirect('/')
                    
                item = Product.objects.get(id=item_id)
                if not item: return HttpResponseRedirect('/')
                if action == 'add_to_wishlist':
                    user.user_products.append(item_id)
                    user.save()

                elif action == 'delete':
                    user.user_products.pop(getindex(user.user_products, item_id))
                    user.save()
                    return HttpResponseRedirect('/cards')

            except Product.DoesNotExist:
                pass
    else:
        return HttpResponseRedirect('/login/')
    
    return HttpResponseRedirect('/')
def getindex(a:array,b:str):
    c = 0
    for i in a:
        if i == b:
            return c
        c += 1
    return 0