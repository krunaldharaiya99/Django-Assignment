# Rest Framework imports
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.permissions import IsStaffOrReadOnly, IsStaffAutherization, IsSuperUserAutherization

# Import models
from products.models import Product

# Import serializers
from products.serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)
        # send django signal

product_create_view = ProductCreateAPIView.as_view()

class ProductListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsStaffOrReadOnly] 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)
        # send django signal

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    """
    Product List API View
    """
    permission_classes = [IsStaffOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk'

product_list_view = ProductListAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsStaffAutherization] # Only Staff member can Update
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        return super().perform_update(serializer)

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsStaffAutherization] # Only Staff member can Delete
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()