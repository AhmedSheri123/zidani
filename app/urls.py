from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

from django.urls import path
from .views import *
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', index, name='index'),
    path('register/', SignupView.as_view(), name='register'),
    path('register/login/', authViews.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('register/logout/', Logout, name='logout'),
    path('register/change-password/', authViews.PasswordChangeView.as_view(template_name='auth/password_change.html',success_url='done/'), name='password-change'),
    path('register/change-password/done/', authViews.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'), name='password-change-done'),
    path('search/', Search.as_view(), name='search'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('add/', add, name='add'),
]