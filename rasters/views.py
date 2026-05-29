from rest_framework import viewsets
from .models import RasterLayer
from .serializers import RasterLayerSerializer

class RasterLayerViewSet(viewsets.ModelViewSet):
    queryset = RasterLayer.objects.all().order_by('-uploaded_at')
    serializer_class = RasterLayerSerializer