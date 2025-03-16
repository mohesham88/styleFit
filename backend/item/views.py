from django.shortcuts import render

from google import genai

# Create your views here

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import ItemSerializer


class ItemUploadView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ItemSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
