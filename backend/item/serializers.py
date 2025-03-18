from bson import ObjectId
from django.contrib.auth.middleware import get_user
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework_mongoengine.serializers import DocumentSerializer


from .models import Item
import cloudinary.uploader
from rest_framework import serializers
from .models import Item
import jwt
from django.conf import settings

from .utils import item_generator


class ItemSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    image_url = serializers.CharField(read_only=True)  # Store Cloudinary URL
    image = serializers.ImageField(write_only=True)  # Only accept image input

    def create(self, validated_data):
        user_id = self.context["request"].user_id
        image = validated_data.pop("image")

        # Upload image to Cloudinary
        upload_result = cloudinary.uploader.upload(image)
        image_url = upload_result["secure_url"]

        newItem = item_generator(image, image_url, user_id)


        # Create ClothingItem with default values
        clothing_item = Item(**newItem)
        clothing_item.save()
        return clothing_item


class ItemListSerializer(DocumentSerializer):

    class Meta:
        model = Item
        fields = '__all__'
