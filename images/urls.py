from django.urls import path

from account.urls import urlpatterns
from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    path('', views.image_list, name='list'),
path('', views.image_list2, name='list2'),
]