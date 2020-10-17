from django.urls import path
from . import views

urlpatterns = [path("", views.route), path("random_word", views.random)]
