from django.urls import path, include
from .views import TestView

urlpatterns = [
    path("list", TestView.as_view(), name="list"),
]