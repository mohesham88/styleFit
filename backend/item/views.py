from bson import ObjectId
from django.shortcuts import render

from google import genai

# Create your views here

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics

from .models import Item
from .serializers import ItemSerializer , ItemListSerializer



class ItemUploadView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ItemSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailView(APIView):
    def get(self, request, item_id):
        try:
            serializer = ItemListSerializer(item_id)  # Serialize the item
            return Response(serializer.data)  # Return the serialized data
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




