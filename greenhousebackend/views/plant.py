from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from greenhousebackend.models import Plant, PlantTag, Tag

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class PlantView(viewsets.ViewSet):
    """retrieves all plants ordered by name"""
    def list(self, request):
        queryset = Plant.objects.all().order_by('name')
        
        tags = request.query_params.get('tags', None)
        if tags is not None:
            queryset = Plant.objects.filter(planttag__tag_id=tags)
        
        serializer = PlantSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PlantSerializer(data=request.data)
        tag = Tag.objects.get(pk=request.data['tags'])
        
        if serializer.is_valid():
            plant = serializer.save()
        
            PlantTag.objects.create(
                plant = plant,
                tag = tag,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Plant.objects.all()
        plant = get_object_or_404(queryset, pk=pk)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Plant.objects.all()
        plant = get_object_or_404(queryset, pk=pk)
        serializer = PlantSerializer(plant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Plant.objects.all()
        plant = get_object_or_404(queryset, pk=pk)
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)