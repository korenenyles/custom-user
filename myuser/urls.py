from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('signup/', views.signUpView, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logout_view, name='logout')
    
]