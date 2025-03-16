from django.urls import path
from .views import ItemUploadView

urlpatterns = [
    path('upload/', ItemUploadView.as_view(), name='item-upload'),
]