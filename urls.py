from django.urls import path
from . import views



urlpatterns = [
    
    path('hello/',views.hello),
    path('signin/',views.signin),
    path('login/',views.login),
    path('logout/',views.logout),
    path('profile/',views.Profile),
    path('account/',views.account,name="account"),
]