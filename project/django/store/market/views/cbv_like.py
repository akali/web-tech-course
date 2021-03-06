from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from market.models import Item, Like
from market.serializers import LikeSerializer
from rest_framework.response import Response


def getOwner(request):
    token = request.headers.get('Authorization')
    if token is None:
        return None
    token = token.split(' ')[1]
    owner = Token.objects.get(key=token).user
    return owner


class LikeApiView(APIView):

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        author = getOwner(request)
        if author is not None:
            if serializer.is_valid():
                item_id = serializer.validated_data.pop('item_id')
                item = Item.objects.get(pk=item_id)
                like = Like.objects.filter(item=item, author=author)
                if like.count() == 0:
                    like = serializer.save(item_id=item_id, author=author)
                    item.likes_count = item.likes_count + 1
                    item.save()
                else:
                    like = Like.objects.get(item=item, author=author).delete()
                    item.likes_count = item.likes_count - 1
                    item.save()
                return Response({
                    'like_count': item.likes_count
                })
            else:
                return Response(serializer.error_messages, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({
            'errors': 'not allowed'
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request):
        author = getOwner(request)
        print(request.data)
        serializer = LikeSerializer(data=request.data)
        if author is not None:
            if serializer.is_valid():
                item_id = serializer.validated_data.pop('item_id')
                item = Item.objects.get(pk=item_id)
                like = Like.objects.filter(item=item, author=author)
                if like.count() != 0:
                    item.likes_count -= 1
                    item.save()
                    like = Like.objects.get(item=item, author=author)
                    like.delete()
                    return Response(like.as_dict())
                return Response({'error': 'Like does not exist'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(serializer.error_messages, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'error': 'No auth header'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
