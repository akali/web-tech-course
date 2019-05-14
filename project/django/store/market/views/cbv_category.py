from django.http import Http404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from market.models import Category
from market.serializers import CategorySerializer


class CategoryApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class CategoryApi(APIView):
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

