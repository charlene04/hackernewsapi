
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from . serializers import *
from django.db.models import Q
import requests



def test(request):
    return Response({"status":"API in good health"})

class topstories(APIView):
    # get all items and also filter
    def get(self, request):
        text = request.GET.get('text', None)
        type = request.GET.get('type', None)
        if text and not type:
            data = Item.objects.filter(Q(title__icontains = text) | Q(text__icontains = text) | Q(by__icontains = text)).order_by('-id')
            item_serializer = itemSerializer(data, many=True)
            return Response(item_serializer.data)
        elif not text and type:
            data = Item.objects.filter(type = type).order_by('-id')
            item_serializer = itemSerializer(data, many=True)
            return Response(item_serializer.data)
        elif text and type:
            data = Item.objects.filter(Q(title__icontains = text) | Q(text__icontains = text) | Q(by__icontains = text), type = type).order_by('-id')
            item_serializer = itemSerializer(data, many=True)
            return Response(item_serializer.data)
        else:
            data = Item.objects.all().order_by('-id')
            item_serializer = itemSerializer(data, many=True)
            return Response(item_serializer.data)

    # Create a customized item
    def post(self, request):
        print(request.data)
        itemdata = request.data
        itemdata["custom"] = True
        item_serializer = postSerializer(data=itemdata)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response(item_serializer.data, status.HTTP_201_CREATED)
        return Response(item_serializer.errors, status.HTTP_400_BAD_REQUEST)


    # Update one custom item only
    def put(self, request, id):
        try:
            item = Item.objects.get(id=id)
            if not item.custom:
                return Response({"message": "update not allowed"}, status.HTTP_401_UNAUTHORIZED)
            for k, v in request.data:
                item.update_fields(k, v)
            item.save(update_fields=request.data.keys())
            return Response({"message": "successfully updated"}, status.HTTP_200_OK)
        except ObjectDoesNotExist:
            item = Item.objects.get(item_id=id)
            if not item.custom:
                return Response({"message": "update not allowed"}, status.HTTP_401_UNAUTHORIZED)
            for k, v in request.data.items():
                item.update_fields(k, v)
            item.save(update_fields=request.data.keys())
            return Response({"message": "successfully updated"}, status.HTTP_200_OK)

        except:
            return Response({"message": "item not found"}, status.HTTP_400_BAD_REQUEST)   
        
    # Delete one custom item
    def delete(self, request, id):
        try:
            item = Item.objects.get(id=id)
            if not item.custom:
                return Response({"message": "item delete not allowed"}, status.HTTP_401_UNAUTHORIZED)
            item.delete()
            return Response({"message": "successfully deleted"}, status.HTTP_200_OK)
        except:
            return Response({"message": "item not found"}, status.HTTP_400_BAD_REQUEST)   
       




  

    