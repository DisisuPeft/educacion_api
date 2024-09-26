from django.db.transaction import commit
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics, status
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data['email']

    password = request.data['password']

    if email is None or password is None:
        return Response({"message": "Por favor, proporciona un email y una contraseña."},
                        status=status.HTTP_400_BAD_REQUEST)

    if not User.objects.filter(email=email).exists():
        return Response({"message": "Usuario no encontrado."},
                        status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, email=request.data['email'])

    if not user.check_password(request.data['password']):
        return Response({"message": "La contraseña es incorrecta."},
                        status=status.HTTP_400_BAD_REQUEST)

    token = Token.objects.get(user=user)

    s = UserSerializer(user)
    # print(token)
    return Response({"token": token.key, "user": s.data}, status=status.HTTP_200_OK)
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
            "message": "Registrado con exito. Inicia sesión!"
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({'Nos devuelve el request': request.user})
# class CreateUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]