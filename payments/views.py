from rest_framework.generics import GenericAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.views import Request, Response

from users.permissions import CustomerAccess
from rest_framework.authentication import TokenAuthentication
from .models import PaymentInfo
from .serializers import PaymentInfoSerializer


class PaymentInfoView(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomerAccess]

    serializer_class = PaymentInfoSerializer
    queryset = PaymentInfo.objects

    def post(self, request: Request):
        serialized: ModelSerializer = self.get_serializer(data=request.data)
        serialized.is_valid(True)
        serialized.save()

        return Response(serialized.data, HTTP_201_CREATED)

    def get(self, _:Request):
        payments_serialized = self.get_serializer(self.get_queryset(), many=True)

        return Response(payments_serialized.data, HTTP_200_OK)