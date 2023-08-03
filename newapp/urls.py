from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('givetest/<int:category_id>',views.givetest ,name = 'givetest'),
    path('add_question/', views.add_question, name='add_question'),
    path('add_question/<int:categories>/', views.add_question, name='add_question'),
    path('test_category_filter/', views.test_category_filter, name='test_category_filter'),



    

]
