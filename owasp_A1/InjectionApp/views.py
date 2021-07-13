from django.shortcuts import render
from django.http.response import HttpResponse

from .models import Users


def user_login(request):
    authentication_error = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # SQL запрос нормального человека:
        # if Users.objects.raw(
        #   "SELECT * FROM InjectionApp_users WHERE username = %s AND password = %s", [username, password]):

        # SQL запрос курильщика:
        # print(Users.objects.all())  # должен хоть что-то вывести
        # print(Users.objects.raw(f"SELECT * FROM InjectionApp_users WHERE username = '{username}' AND password = '{password}';"))  # сам запрос
        # print(bool(Users.objects.raw(f"SELECT * FROM InjectionApp_users WHERE username = '{username}' AND password = '{password}';")))  # True если прошло
        if username == 'admin' and Users.objects.raw(
                f"SELECT * FROM InjectionApp_users WHERE username = '{username}' AND password = '{password}';"):
            return HttpResponse(content='SQLflag01192injection')
        else:
            authentication_error = True

    return render(request, 'InjectionApp/user_login.html', {'authentication_error': authentication_error})
