from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import rest_framework.status as status
from .serializers import LoginSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                data={"error": "ususario no valido"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        token = Token.objects.get_or_create(user=user)
        # serielizer = AuthTokenSerializer(token)
        print(token.key)
        return Response(data={"token": token.key}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
