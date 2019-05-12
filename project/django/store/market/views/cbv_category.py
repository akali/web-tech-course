from rest_framework import status, generics

from market.models import Category
from market.serializers import CategorySerializer


class CategoryApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
