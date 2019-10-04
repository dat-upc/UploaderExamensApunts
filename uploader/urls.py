from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('signup',  views.signup, name='signup'),
    path('signup/', views.perform_signup, name='perform_signup'),
]