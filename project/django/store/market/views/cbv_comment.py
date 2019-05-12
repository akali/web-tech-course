from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from market.models import Comment, Item
from market.serializers import CommentSerializer


def getOwner(request):
    token = request.headers.get('Authorization')
    token = token.split(' ')[1]
    owner = Token.objects.get(key=token).user
    return owner


class CommentApi(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


    def post(self, request):
        owner = getOwner(request)
        print(owner)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save(author=owner)
            comment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CommentWithIdApi(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        owner = getOwner(request)
        if owner.id == comment.owner.id:
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=owner)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        owner = getOwner(request)
        comment = self.get_object(pk)
        if owner.id == comment.owner.id:
            comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
