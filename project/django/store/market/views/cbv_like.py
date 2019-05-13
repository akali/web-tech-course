from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from market.models import Item, Like
from market.serializers import LikeSerializer
from rest_framework.response import Response


def getOwner(request):
    token = request.headers.get('Authorization')
    token = token.split(' ')[1]
    owner = Token.objects.get(key=token).user
    return owner


class LikeApiView(APIView):

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        author = getOwner(request)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=author)
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        author = getOwner(request)
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            item_id = serializer.validated_data.pop('item_id')
            item = Item.objects.get(pk=item_id)
            like = Like.objects.get(item=item, author=author)

            if like is not None:
                item.likes_count -= 1
                item.save()
                like.delete()
                return Response(like.as_dict())
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)