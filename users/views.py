from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED,
)
from rest_framework.views import Request, Response

from .models import Users
from .permissions import IsAdmin
from .serializers import LoginSerializer, UserSerializer


class UserView(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]

    serializer_class = UserSerializer
    queryset = Users.objects

    def post(self, request: Request):
        serialized: ModelSerializer = self.get_serializer(data=request.data)
        serialized.is_valid(True)

        user: Users = Users.objects.create(**serialized.validated_data)
        user.set_password(serialized.validated_data["password"])
        user.save()

        out_serialize: ModelSerializer = self.get_serializer(user)

        return Response(out_serialize.data, HTTP_201_CREATED)
            

    def get(self, _: Request):
        users = self.get_queryset()

        out_serialize: ModelSerializer = self.get_serializer(users, many=True)

        return Response(out_serialize.data, HTTP_200_OK)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request: Request):
        serialized: ModelSerializer = self.get_serializer(data=request.data)
        serialized.is_valid(True)

        user = authenticate(**serialized.validated_data)

        if not user:
            return Response({"message": "Invalid credentials."}, HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, HTTP_200_OK)