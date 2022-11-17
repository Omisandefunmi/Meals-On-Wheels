from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

class SignUpApiView(APIView):

    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer)
            serializer.save()
        else:
            return Response({"details": "There was an error saving this user. PLEASE TRY AGAIN"}, status=HTTP_403_FORBIDDEN)
        return Response({"details": serializer.data}, status=status.HTTP_200_OK)
        

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data={
                "username": request.data.get("email"),
                "password": request.data.get("password")
            },
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        print("Token ===> ", token.key)
        print("created ===> "+created)
        return Response(
        {
            "key": token.key,
            "user": UserSerializer(user).data,
        },
        status=status.HTTP_202_ACCEPTED
        )
