from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Sense-Home'),
    path('about/', views.about, name='Sense-About'),
    path('signup.html/', views.signup, name='Sense-SignUp'),

]
