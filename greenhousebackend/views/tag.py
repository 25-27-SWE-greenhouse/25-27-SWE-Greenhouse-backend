"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from greenhousebackend.models import Tag


class TagView(ViewSet):
    """Green House tag view"""

    def retrieve(self, request, pk):
        tag = Tag.objects.get(pk=pk) 
        serializer = TagSerializer(tag)
        return Response(serializer.data)


    def list(self, request):
        tags = Tag.objects.all()
        
        plant = request.query_params.get('plant', None)
        if plant is not None:
            tags = Tag.objects.filter(planttag__plant_id=plant)
        
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """

        tag = Tag.objects.create(
            name=request.data["name"],
        )
        serializer = TagSerializer(tag)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        tag = Tag.objects.get(pk=pk)
        tag.name = request.data["name"]

        tag.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Tag
        fields = ('id', 'name')