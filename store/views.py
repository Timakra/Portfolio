from django.shortcuts import render ,get_object_or_404,redirect
from django.http import HttpResponse
from store.models import storeItems,Specs,CartItem
from store.forms import registerForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def distinct(list):
    result = []
    list.sort
    for item in list:
        if item not in result:
            result.append(item)
    return result

def defaultCatgories():
    categories = distinct(list(storeItems.objects.all().values_list('category', flat=True)))
    return categories

def home(request):
    storeitems = storeItems.objects.all()
    categories = defaultCatgories()
    content = {"storeItems":storeitems,"categories":categories,'user':request.user}
    
    return render(request,"store/storeindex.html",content)

def itemdetail(request,skunum):
    skunum = int(skunum)
    categories = defaultCatgories()
    item = get_object_or_404(storeItems, sku=skunum)
    specs = Specs.objects.filter(item__sku=item.sku)

    content = {"item":item,"categories":categories,"specs":specs}
    return render(request,"store/itemdetail.html",content)


def register(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/store')

    else:
        form = registerForm()
    content = { 'form':form }
    return render(request,"store/register.html",content)

def cart(request):
    cartitems = CartItem.objects.filter(user= request.user)
    if cartitems:
        content = {"cart":cartitems}
        return render(request,'store/cart.html',content)
    return render(request,'store/cart.html')

@csrf_exempt
def tocart(request,count=1):
    if request.method == "POST":
        skunum = int(request.POST['sku'])
        storeitem = storeItems.objects.filter(sku=skunum)[0]
        cart = CartItem.objects.filter(user=request.user,item=storeitem)
        if cart:
            cart = CartItem.objects.get(user=request.user,item=storeitem)
            cart.quantity += 1
            cart.totalprice = cart.quantity * cart.item.price
            cart.save()
            return  HttpResponse(request)
        else:
            CartItem.objects.create(user = request.user ,item=storeitem,quantity = count,totalprice = storeitem.price)
            return  HttpResponse(request)

def catgories(request,category):
    items = storeItems.objects.filter(category = category)
    categories = defaultCatgories()
    content = {"storeItems":items,"categories":categories,"category" : category}
    return render(request,"store/categories.html",content)
    

def profile(request):
    return render(request,"store/profile.html")
