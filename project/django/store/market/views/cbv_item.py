from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from market.models import Item
from market.serializers import ItemSerializer


def getOwner(request):
    token = request.headers.get('Authorization')
    token = token.split(' ')[1]
    owner = Token.objects.get(key=token).user
    return owner


class ItemApiView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        owner = getOwner(request)
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            item = serializer.save(owner=owner)
            item.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ItemWithIdApiView(APIView):

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(instance=item, data=request.data)
        owner = getOwner(request)
        if owner.id == item.owner.id:
            if serializer.is_valid(raise_exception=True):
                serializer.save(owner=owner)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        owner = getOwner(request)
        item = self.get_object(pk)
        if owner.id == item.owner.id:
            item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
