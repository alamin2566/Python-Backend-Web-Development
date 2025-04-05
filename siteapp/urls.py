from django.urls import path
from.import views


urlpatterns = [
    path('',views.index),
    path('counter',views.counter),
    path('register',views.register),
    path('login',views.login),
    path('post/<str>:id',views.post)
]
