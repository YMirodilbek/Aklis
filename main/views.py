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
    return render(request,'about.html')


def Contact(request):
    return render(request,'contact.html')

def SendForm(request):
    if request.method == "POST":
        ismfamilya = request.post['ismfamilya']
        pochta = request.post['pochta']
        telfon = request.post['telfon']
        murojaat_sababi = request.post['murojaat_sababi']
        text = request.post['text']
        date = request.post['date']

        ContactForm.objects.create(ismfamilya=ismfamilya,pochta=pochta,telfon=telfon,murojaat_sababi=murojaat_sababi,text=text,date=date)
        return redirect(request,'/sms.html/')