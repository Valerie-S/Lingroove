from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # if path is empty, return the index page
    path('signup/', views.signup, name='signup'),
]