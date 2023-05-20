from django.urls import path
from . import views

urlpatterns = [
    path('getPosts/', views.getPosts),
    path('addPost/',views.addPost),
    path('updatePost/',views.updatePost),
    path('getPost/',views.getPost),
]