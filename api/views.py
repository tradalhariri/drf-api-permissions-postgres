from rest_framework import generics
from items.models import Item
from .serializers import ItemSerializer
from .permissions import IsOwnerOrReadOnly

class ItemAPIView(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ItemDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer