import json

from django.template import Context
from rest_framework import serializers

from chat.utils import generate_serpapi_params, get_product_link
from item.models import Item
from item.serializers import ItemSerializer, ItemListSerializer
from serpapi.google_search import GoogleSearch









class OutfitSerializer(serializers.Serializer):\

    items = serializers.ListField(
        child=serializers.CharField()  # Assuming the item IDs are sent as strings (ObjectId as string)
    )
    suggestions = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )

    description = serializers.CharField()



    def to_representation(self, instance):
        items = ItemListSerializer(instance["items"], many=True).data
        print(items)
        user_gender = self.context.get("user_gender")
        print(user_gender)

        description = instance.get("description")

        buy_suggestions = []
        if instance.get("suggestions"):
            suggestions = instance["suggestions"]
            for suggestion in suggestions:
                search_result = GoogleSearch(generate_serpapi_params(suggestion + " " + "men" , "Egypt"))
                top_product = search_result.get_dict()["immersive_products"][0]

                product = {
                    "thumbnail" : top_product["thumbnail"],
                    "title" : top_product["title"],
                    "price" : top_product["price"],
                    "source" : top_product["source"],
                    "source_logo" : top_product["source_logo"],
                    "link" : get_product_link(top_product["serpapi_product_api"])
                }

                buy_suggestions.append(product)


        return {
            "description" : description,
            "items": items,
            "buy_suggestions" : buy_suggestions,
        }