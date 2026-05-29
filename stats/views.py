from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import AnalysisResult
from .serializers import AnalysisResultSerializer

class AnalysisResultViewSet(viewsets.ModelViewSet):
    queryset = AnalysisResult.objects.all()
    serializer_class = AnalysisResultSerializer

    @action(detail=False, methods=['get'])
    def by_type(self, request):
        result_type = request.query_params.get('type')
        results = AnalysisResult.objects.filter(result_type=result_type)
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)