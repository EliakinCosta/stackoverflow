from rest_framework import serializers
from . import models


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Picture
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(source='picture_set', many=True, read_only=True)

    class Meta:
        model = models.Album
        fields = '__all__'
