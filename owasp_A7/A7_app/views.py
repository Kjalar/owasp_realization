from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout
from .forms import UserLoginForm
from .models import UsersData


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('get_acc', user.pk)
    else:
        form = UserLoginForm()
    return render(request, 'A7_app/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def get_acc(request, user_id):
    if request.user.is_authenticated:
        try:
            data = UsersData.objects.get(user_id=user_id).data
        except ObjectDoesNotExist or MultipleObjectsReturned:
            data = None
        return render(request, 'A7_app/index.html', {'data': data, 'username': request.user.username})
    else:
        return HttpResponse()
