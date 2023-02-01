from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('layout/',views.layout,name = 'layout'),
    path('table/',views.new_applicants,name = 'table'),
    path('signup/',views.signup,name = 'signup'),
    path('login/',views.login,name = 'login'),
    path('create',views.create,name = 'create'),



]