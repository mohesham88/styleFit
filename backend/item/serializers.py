from bson import ObjectId
from rest_framework import serializers
from rest_framework.exceptions import NotFound

from utils.utils import serialize_mongo_document
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
        return clothing_item


class ItemListSerializer(serializers.Serializer):

    def get_item(self, item_id):
        """
        Fetch the item from MongoDB based on the provided item_id.
        """
        try:
            # Convert item_id to ObjectId
            item = Item.objects.get(id=ObjectId(item_id))
            return item
        except Item.DoesNotExist:
            raise NotFound(detail="Item not found.")

    def to_representation(self, item_id):
        item_document = self.get_item(item_id)
        item = serialize_mongo_document(item_document)
        return item
