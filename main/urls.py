from django.urls import path, include

from main import views




# main/urls.py
from django.urls import path
from main import views



app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('services_index/', views.services_index, name="services_index"),
    path('about_index/', views.about_index, name="about_index"),

    # path('password_reset/', views.password_reset_request, name='password_reset'),
    # path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', views.password_reset_complete, name='password_reset_complete'),

]