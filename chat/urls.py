from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.Registration.as_view(), name='registration'),
    path('', views.Login.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('index/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
]
