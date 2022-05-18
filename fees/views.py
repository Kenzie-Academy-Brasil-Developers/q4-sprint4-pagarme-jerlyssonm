from django.core.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_404_NOT_FOUND)
from rest_framework.views import Request, Response

from .models import Fees
from .serializers import FeeSerializer


class FeesView(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = FeeSerializer
    queryset = Fees.objects


    def post(self, request: Request):
        serialized: ModelSerializer = self.get_serializer(data=request.data)

        serialized.is_valid(True)
        serialized.save()

        return Response(serialized.data, HTTP_201_CREATED)

    def get(self, _: Request, fee_id= ""):

        try:
            fees = self.get_serializer(self.get_queryset(), many=True)

            if fee_id:
                fee_found = Fees.objects.get(id=fee_id)
                fee_serialized = self.get_serializer(fee_found)
                
                return Response(fee_serialized.data, HTTP_200_OK)

            return Response(fees.data, HTTP_200_OK)

        except ValidationError:
            return Response({"message": "fee not found"}, HTTP_404_NOT_FOUND)

        