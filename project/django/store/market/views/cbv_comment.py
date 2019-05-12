from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from market.models import Comment, Item
from market.serializers import CommentSerializer


class CommentApi(APIView):
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            comment = serializer.save(item=Item.objects.get(pk=pk))
            comment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, pk):
        # comments = self.get_object(pk).all()
        comments = self.get_object(pk).comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
