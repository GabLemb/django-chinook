from rest_framework import serializers
from .models import Albums, Artists, Tracks, Playlists


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = "__all__"


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = "__all__"


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = "__all__"
