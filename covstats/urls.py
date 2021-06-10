from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.cases,name='cases'),
    path('vaccine',views.vaccine,name='vaccine')
]