from django.urls import path
from . import views
from newapp import views as newappviews

app_name = "accounts"


urlpatterns = [
     path('',views.LoginPage , name='login'),
    path('login/',views.LoginPage , name='login'),
    path('signup/',views.registration_view, name='signup'),
    path('custom_login/',views.LoginPage, name='custom_login'),
    path('logout/',views.LogoutPage, name='logout'),

    

]
