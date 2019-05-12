from rest_framework import status
from rest_framework.views import APIView
from store.market.models import Like
from store.market.serializers import LikeSerializer, LikeIdSerializer
from rest_framework.response import Response


class Like(APIView):

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):

        serializer = LikeIdSerializer(data=request.data)

        if serializer.is_valid():
            like = Like.objects.get(
                author_id=serializer.author_id,
                item_id=serializer.item_id
            )

            something = like.delete()

            return Response(something)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
