from rest_framework import serializers
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
        token = self.context['request'].headers['Authorization'].split()[1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("id")

        image = validated_data.pop("image")

        # Upload image to Cloudinary
        upload_result = cloudinary.uploader.upload(image)
        image_url = upload_result["secure_url"]

        newItem = item_generator(image, image_url, user_id)


        # Create ClothingItem with default values
        clothing_item = Item(**newItem)
        clothing_item.save()
        print(clothing_item)
        return clothing_item

