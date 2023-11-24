from django.urls import path, include
from .views import *

urlpatterns = [
    path("users/", user_list, name="user-list"),
    path("users/<int:pk>/", user_detail, name="user-detail"),
]
