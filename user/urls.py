from django.urls import path
from product import views
from . views import *
urlpatterns = [
    # please connect the user app with project ecommerce through settings
    #views.home le product ko views taanxa register_user le user ko views nai
    path("", views.home, name="home"),
    path("register/", register_user, name='register'),
    path("login/", login_user, name='login'),
]