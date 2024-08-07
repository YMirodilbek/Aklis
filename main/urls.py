from django.urls import path,include
from .views import *
from django.conf.urls.i18n import i18n_patterns

urlpatterns=[
    path('',Index , name="index"),
    path('about/',About,name="about"),
    path('contact/',Contact,name="about"),
    path('send/',SendForm),
    path('team/',Team),
    path('e404/',Error),
    path('product/',Product1,name="product"),
    path('i18n/en/',include("django.conf.urls.i18n")),
    path('i18n/uz/',include("django.conf.urls.i18n")),
    path('i18n/ru/',include("django.conf.urls.i18n")),

]