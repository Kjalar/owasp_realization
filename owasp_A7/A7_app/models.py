from django.db import models


class UsersData(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.TextField()

