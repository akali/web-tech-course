from django.http import Http404
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from market.models import Comment, Item
from market.serializers import CommentSerializer


def getOwner(request):
    token = request.headers.get('Authorization')
    token = token.split(' ')[1]
    owner = Token.objects.get(key=token).user
    return owner


class CommentApiView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        owner = getOwner(request)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save(author=owner)
            comment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)