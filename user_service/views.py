from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer
from .models import User

# User registration example 
@api_view(['POST'])
def register(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login view with token generation 
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
  username = request.data.get('username')
  password = request.data.get('password')

  if not username or not password:
    return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

  try:
    user = User.objects.get(username=username)
  except User.DoesNotExist:
    return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

  if not user.check_password(password):
    return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

  # Login successful, generate and return token (replace with your token generation logic)
  token, _ = Token.objects.get_or_create(user=user)
  return Response({'token': token.key}, status=status.HTTP_200_OK)

# Update user profile view
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request):
  user = request.user  # Access the authenticated user

  serializer = UserSerializer(user, data=request.data, partial=True)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

