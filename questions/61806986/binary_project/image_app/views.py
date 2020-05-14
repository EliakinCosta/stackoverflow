from django.shortcuts import render
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class AlbumList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self,request):
        albums = models.Album.objects.all()
        serializer = serializers.AlbumSerializer(albums, many=True)
        return Response(serializer.data)
