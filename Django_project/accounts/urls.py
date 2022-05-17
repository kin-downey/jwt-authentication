from django.urls import path
from .views import *


urlpatterns = [
    path('users/', UserList.as_view()),
    path('test/', SampleView.as_view()),
]
