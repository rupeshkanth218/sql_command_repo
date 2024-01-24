from django.urls import path
from .views import home,de
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    #path('',CommandList.as_view(),name='home'),
    #path('detail/<int:pk>',DetailCommand.as_view(),name= "details"),
    
    path("auth/login/", LoginView.as_view(template_name="registration/login.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path('',home,name = "home"),
    path('detail/<int:pk>',de,name = "details"),
    
]
