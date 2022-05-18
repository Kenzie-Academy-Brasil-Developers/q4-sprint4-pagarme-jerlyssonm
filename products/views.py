from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import Request, Response
from rest_framework.serializers import ModelSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK,HTTP_404_NOT_FOUND
from users.models import Users

from users.permissions import OnlySellerAccess

from .models import Products
from .serializers import ProductSerializer, ProductPatchSerializer

class ProductView(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OnlySellerAccess]
    
    serializer_class = ProductSerializer
    queryset = Products.objects

    def post(self, request: Request):
        serialized: ModelSerializer = self.get_serializer(data=request.data)

        serialized.is_valid(True)
        serialized.save()

        return Response(serialized.data, HTTP_201_CREATED)

    def get(self, _: Request, product_id=""):

        try:
            products = self.get_serializer(
                self.get_queryset(), many=True
                )

            if product_id:
                product = Products.objects.get(id=product_id)

                product_serialize = self.get_serializer(product)

                return Response(product_serialize.data, HTTP_200_OK)
            
            return Response(products.data, HTTP_200_OK)

        except ValidationError:
            return Response({"message": "Invalid product id"}, HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({"message": "Product does not exist"}, HTTP_404_NOT_FOUND)

    def patch(self, request: Request, product_id: str = ""):
        try:
            serialized: ModelSerializer = ProductPatchSerializer(data=request.data)
            serialized.is_valid(True)

            product_found = Products.objects.filter(pk=product_id)

            if not product_found:
                raise ObjectDoesNotExist
            
            product_found.update(**serialized.data)

            product_serialize = self.get_serializer(product_found.first())

            return Response(product_serialize.data, HTTP_200_OK)

        except ValidationError:
            return Response({"message": "Invalid product id"}, HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({"message": "Product does not exist"}, HTTP_404_NOT_FOUND)


class GetPerSellerView(GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, _: Request, seller_id= ""):

        try:
            seller: Users = Users.objects.get(id=seller_id)

            if not seller or not seller.is_seller:
                raise ObjectDoesNotExist

            products = Products.objects.filter(seller_id=seller_id)

            products_serialize = self.get_serializer(products, many=True)

            return Response(products_serialize.data, HTTP_200_OK)

        except ValidationError:
            return Response({"message": "Invalid seller id"}, HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({"message": "Seller does not exist"}, HTTP_404_NOT_FOUND)
