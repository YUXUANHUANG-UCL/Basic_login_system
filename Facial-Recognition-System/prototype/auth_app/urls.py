from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('facial_auth/', views.facial_auth, name='facial_auth'),
    path('umain/', views.umain, name='umain'),
    path('settings/', views.settings, name='settings'),
    path('editordel/', views.editordel, name='editordel'),
]

