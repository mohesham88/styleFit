from django.urls import path
from .views import ItemUploadView, ItemDetailView

urlpatterns = [
    path('upload/', ItemUploadView.as_view(), name='item-upload'),
    path('<str:item_id>/', ItemDetailView.as_view(), name='item-detail'),
]