from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('login/',views.LogIn,name='login'),
    path('logout/',views.LogOut,name='logout'),
    path('signup/',views.SignUp,name='signup'),
    path('EditInfo/',views.EditUserInfo,name='Edit'),
    path('Books/',views.Books,name='Books'),
    path('BookSearch/',views.BookSearch,name='BookSearch'),
    path('BorrowBook/',views.BorrowBook,name='BorrowBook'),
    path('HomePage/',views.UserHomePage,name='HomePage'),

]