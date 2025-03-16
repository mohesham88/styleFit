from bson import ObjectId


def serialize_mongo_document(document):
    """
        Serializes a MongoEngine document, converting all ObjectId fields to strings.

        Args:
            doc: A MongoEngine document instance.

        Returns:
            dict: The serialized document with ObjectId fields converted to strings.
        """
    representation = {}
    for field_name, field_value in document.to_mongo().items():
        if isinstance(field_value, ObjectId):
            # Convert ObjectId to string if it's an ObjectId
            field_value = str(field_value)
        # Add the field to the representation
        representation[field_name] = field_value
    return representation