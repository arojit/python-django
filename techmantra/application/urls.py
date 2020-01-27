from django.urls import path
# from django.urls import admin
from . import views

urlpatterns = [
    path('fetch-user',views.fetchUser,name='fetchUser'),
]
