from django.urls import path
from .views import *

urlpatterns=[
    path('',Index),
    path('about/',About),
    path('contact/',Contact),
    path('send/',SendForm),
    path('team/',Team),
    path('e404/',Error),
    path('product/',Product)

]