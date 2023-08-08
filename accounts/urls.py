from django.urls import path
from . import views
from newapp import views as newappviews

urlpatterns = [
    path('',newappviews.home , name='home'),
    path('signup/',views.registration_view, name='signup'),
    path('login/',views.LoginPage, name='login'),
    path('logout/',views.LogoutPage, name='logout'),

    

]
