from rest_framework import serializers
from .models import Item
import cloudinary.uploader
from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(source="user.id", read_only=True)
    image_url = serializers.CharField(read_only=True)  # Store Cloudinary URL
    image = serializers.ImageField(write_only=True)  # Only accept image input

    def create(self, validated_data):
        image = validated_data.pop("image")

        # Upload image to Cloudinary
        upload_result = cloudinary.uploader.upload(image)
        image_url = upload_result["secure_url"]

        # Create ClothingItem with default values
        clothing_item = Item.objects.create(
            user=self.context["request"].user, image_url=image_url
        )

        return clothing_item
