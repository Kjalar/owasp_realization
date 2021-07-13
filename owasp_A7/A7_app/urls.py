from django.urls import path

from .views import user_login, user_logout, get_acc


urlpatterns = [
    path('account/<int:user_id>', get_acc, name='get_acc'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]
