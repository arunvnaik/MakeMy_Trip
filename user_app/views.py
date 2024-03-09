from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from user_app.serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated

class UserRegistration(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()  # Delete the user's token
        except Exception as e:
            return Response({'error': 'Failed to logout'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
