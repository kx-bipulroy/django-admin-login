from django.urls import path

from .views import *


urlpatterns = [
    path('', login, name='login'),
    path('do-login', do_login, name='do_login'),
    path('home', home, name='home'),
    path('logout', logout_action, name='logout'),
]
