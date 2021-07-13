from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseBadRequest

from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request, username):
        user_for_delete = User.objects.filter(username=username)

        if user_for_delete:
            user_for_delete.delete()
            return HttpResponse(status=204, content='successful user deletion')
        else:
            return HttpResponseBadRequest()
