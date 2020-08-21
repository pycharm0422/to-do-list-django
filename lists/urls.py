from django.urls import path
from lists import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', views.DeleteList, name='deletes'),
    path('clearitems/', views.clearItems, name='clear-list'),
    path('add_works/', views.createList, name='add-list'),
]