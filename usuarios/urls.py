from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views import login_view

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
