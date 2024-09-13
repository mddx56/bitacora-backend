from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()


class UserAccountView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


"""
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"message": "Agregado correctamente."}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        ser = UserSerializer(users)
        return Response(ser.data)
"""
