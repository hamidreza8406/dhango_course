from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.Signup.as_view(), name='signup')

]



