from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from na_laalii_app.models import mtrlinfo, DEALER, pro
from .forms import mtrlform,dealerform
from random import randint

def home(request):
# Create your views here.
    htop= mtrlinfo.objects.order_by("-cost")[:4]
    hnew=mtrlinfo.objects.order_by('-timestamp')[:4]
    brand=pro.objects.get(id=1)
    context={ "her":"love","htop":htop,"hnew":hnew,"brand":brand,}
    template="na_laalii_app/home.html"
    query=request.GET.get('id')
    if query:
        post=mtrlinfo.objects.get(id=query)
        cat ="home"
        context= {"post":post,"cat":cat}
        template="na_laalii_app/detail.html"
    return render(request,template,context)

def top(request):
    top= mtrlinfo.objects.order_by("-cost")[:12]
    brand=pro.objects.get(id=1)
    context={"top":top,"brand":brand}
    template="na_laalii_app/top.html"
    query=request.GET.get('id')
    if query:
        post=mtrlinfo.objects.get(id=query)
        cat ="top"
        context= {"post":post,"cat":cat}
        template="na_laalii_app/detail.html"
    return render(request,template, context)

def new(request):
    new=mtrlinfo.objects.order_by('-timestamp')[:12]
    brand=pro.objects.get(id=1)
    context={'new':new,"brand":brand}
    template="na_laalii_app/new.html"
    query=request.GET.get('id')
    if query:
        post=mtrlinfo.objects.get(id=query)
        cat ="new"
        context= {"post":post,"cat":cat}
        template="na_laalii_app/detail.html"
    return render(request,template, context)

def registration(request):
    template='na_laalii_app/registration.html'
    brand=pro.objects.get(id=1)
    cookie=request.COOKIES
    context={"brand":brand,"cookie":cookie}
    response=render(request,template, context)
    for cookie in cookie:
        print(cookie)
        if cookie=="Kw":
            response=HttpResponseRedirect("/My_Account/")
    return response

def categories(request):
    template="na_laalii_app/categories.html"
    brand=pro.objects.get(id=1)
    context={'brand':brand,}
    return render(request,template,context)

def loggedin(request,):
    logquery = request.POST.get('login', '')

    reg=DEALER.objects.all()
    context={"reg":reg,}
    if logquery  :
        query = request.POST.get('q', '')
        password = request.POST.get('password', '')
        resp="__"
        if query:
            q=DEALER.objects.get(full_name=query)
        else:
            resp="the user name you have entered is wrong!"
        if q.password==password:
            resp="you have logged in!!"
        else :
            resp="incorrect password"
    account=q.keyword
    response=HttpResponseRedirect("/My_Account/")
    response.set_cookie("Kw",account)
    return response

def registered(request):
    regquery = request.POST.get('register', '')

def account(request):#isnot functional
    key=request.COOKIES['Kw']
    if key=="":
        response=HttpResponseRedirect("/registration/")
    else:
        user=DEALER.objects.get(keyword=key)
        name=user.id
        assets=mtrlinfo.objects.filter(dealer=name)

        context={"user":user,"assets":assets,}
        template='na_laalii_app/account.html'
        response=render(request,template, context)
    return response

def logout(request):
    key=request.COOKIES['Kw']
    response=HttpResponseRedirect("/home/")
    response.delete_cookie("Kw",)
    return response

def get_account(request,key):
    user=DEALER.objects.get(keyword=key)
    name=user.id
    assets=mtrlinfo.objects.filter(dealer=name)
    context={"user":user,"assets":assets}
    template='na_laalii_app/account.html'
    return render(request,template, context)

def add_asset(request):
    key=request.COOKIES['Kw']
    user=DEALER.objects.get(keyword=key)
    dealer=user.full_name
    description = request.POST.get('description', '')
    cost= request.POST.get('cost', '')
    word_address = request.POST.get('word_address', '')
    no_of_rooms = request.POST.get('no_of_rooms','')
    if request.method=="POST":
        mapad = request.FILES['mapp_address']
        frontal_picture=request.FILES["frontal_picture"]
        photo_from_inside = request.FILES['photo_from_inside']
        rooms_in_birdeye = request.FILES['rooms_in_birdeye']
        response=HttpResponseRedirect("/My_Account/")
    new_asset = mtrlinfo(dealer=user,description=description,cost=cost,
        frontal_picture=frontal_picture,word_address=word_address,no_of_rooms=no_of_rooms,
        photo_from_inside=photo_from_inside,rooms_in_birdeye=rooms_in_birdeye)
    new_asset.save()
    return response

def edit_asset(request,desc):
    key=request.COOKIES['Kw']
    user=DEALER.objects.get(keyword=key)
    asset=mtrlinfo.objects.get(description=desc)
    template="na_laalii_app/adit.html"
    context={"user":user,"asset":asset}
    return  render(request,template,context)

def del_asset(request,desc):
    asset=mtrlinfo.objects.get(description=desc)
    asset.delete()
    return HttpResponseRedirect("/My_Account/")

def rooms(request):
    return HttpResponse("rooms")

def location(request):
    return HttpResponse("locations")

def sale(request):
    return HttpResponse("sale")

def cost(request):
    return HttpResponse("cost")

def office(request):
    return HttpResponse("office")

def news(request):
    return HttpResponse("news")
def services(request):
    return HttpResponse("services")
def gojo(request):
    return HttpResponse("gojo")
