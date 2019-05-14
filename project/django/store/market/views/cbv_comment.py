from django.http import Http404
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from market.models import Comment, Item
from market.serializers import CommentSerializer


def getOwner(request):
    token = request.headers.get('Authorization')
    if token is None:
        return None
    token = token.split(' ')[1]
    owner = Token.objects.get(key=token).user
    return owner


class CommentApiView(APIView):
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        item = self.get_object(pk)
        comments = item.comments
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        owner = getOwner(request)
        serializer = CommentSerializer(data=request.data)
        item = self.get_object(pk)
        if owner is not None:
            if serializer.is_valid(raise_exception=True):
                comment = serializer.save(author=owner, item=item)
                comment.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
