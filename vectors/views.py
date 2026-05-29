from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.http import JsonResponse
from .models import VectorLayer
from .serializers import VectorLayerSerializer
import json

class VectorLayerViewSet(viewsets.ModelViewSet):
    queryset = VectorLayer.objects.all().order_by('-uploaded_at')
    serializer_class = VectorLayerSerializer

def serve_geojson(request, layer_id):
    try:
        layer = VectorLayer.objects.get(pk=layer_id)
        with open(layer.file.path, encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data)
    except VectorLayer.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)