from django.db.transaction import commit
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics, status
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    return Response({request})
#
#
#
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # user = User.objects.get(username=request.data['username'])
        # user.set_password(serializer.data['password'])
        # user.save()
        Token.objects.create(user=user)
        return Response({
            "message": "Registrado con exito."
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CreateUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]