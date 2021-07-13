from django.urls import path

from .views import UserView


urlpatterns = [
    path('user/<str:username>', UserView.as_view()),
    path('user/', UserView.as_view()),
]
