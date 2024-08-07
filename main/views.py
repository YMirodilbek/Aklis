from django.shortcuts import render,redirect
# Create your views here.

from .models import *


def Index(request):
    product = Mahsulotlar.objects.all()
    context={
        'product':product,
        'mah1':BizningMahsulot.objects.first(),
        'mah2':BizningMahsulot.objects.last(),
        'mah3':BizningMahsulot.objects.get(id=3),
        'mah4':BizningMahsulot.objects.get(id=2),
        


    }
    return render(request,'index.html',context)

def About(request):
    context={
        'about':AboutAwards.objects.first(),
        'name':AboutName.objects.all(),
        'xodim':Xodimlar.objects.all()
    }
    return render(request,'about.html',context)



def Team(request):
    return render(request,'team.html')


def Contact(request):
    context={
        'info':Info.objects.first()
    }
    return render(request,'contact.html',context)

def SendForm(request):
    if request.method == "POST":
        ismfamilya = request.POST['ismfamilya']
        pochta = request.POST['pochta']
        telfon = request.POST['telfon']
        murojaat_sababi = request.POST['murojaat_sababi']
        text = request.POST['text']

        ContactForm.objects.create(ismfamilya=ismfamilya,pochta=pochta,telfon=telfon,murojaat_sababi=murojaat_sababi,text=text)
        return redirect('/contact/')
    

def Error(request, exception=None):
    return render(request, 'error.html', status=404)

def Product1(request):
    context={
        'product':Product.objects.all()
    }
    return render(request,'product.html',context)