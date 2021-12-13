from django.urls import path
from .views import ItemAPIView, ItemDetailApiView

urlpatterns = [
    path('', ItemAPIView.as_view(), name = 'item_list'),
    path('<int:pk>/', ItemDetailApiView.as_view(),name = 'item_detail'),

]