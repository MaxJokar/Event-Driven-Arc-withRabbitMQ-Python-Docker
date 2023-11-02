from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .producer import publish
from .serializers import ProductSerializer
import random


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):    # GET /api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        # publish() for the first test 
        return Response(serializer.data) 
    
#  POSTMAN , POST (body, raw , json ):   

    def create(self, request):  # POST,raw, json  http://127.0.0.1:8000/api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):       # GET http://127.0.0.1:8000/api/products/1
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None): # POSTMAN PUT , change in http://127.0.0.1:8000/api/products/1
        product = Product.objects.get(id=pk) 
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): # DELETE http://127.0.0.1:8000/api/products/1
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

# in Postman every time we send we get a random number 
class UserAPIView(APIView):   # GET   /api/user POSTMAN:none, Body,
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })

