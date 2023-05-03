from django.urls import path
from . import views

urlpatterns = [
    path('listuser', views.ListUser.as_view(), name='listuser'),
    path('listuser/<int:pk>', views.ListUser.as_view(), name='patchuser')
]