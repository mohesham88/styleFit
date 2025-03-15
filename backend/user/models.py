from mongoengine import Document, StringField, EmailField, DateTimeField
from django.utils.timezone import now

class Profile(Document):
    name = StringField(max_length=50, required=True)
    gender = StringField(max_length=10, required=True)
    email = EmailField(max_length=50, required=True, unique=True)
    password = StringField(max_length=50, required=True)  # Store hashed passwords securely
    created_at = DateTimeField(default=now)
    updated_at = DateTimeField(default=now)

    def __str__(self):
        return self.name
