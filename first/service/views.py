from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Albums, Artists, Tracks, Playlists
from .serializers import (
    AlbumSerializer,
    ArtistSerializer,
    TrackSerializer,
    PlaylistSerializer,
)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = AlbumSerializer
    filterset_fields = ["title"]

    def create(self, request, *args, **kwargs):
        title = request.data.get("title")
        artistid = request.data.get("artistid")
        if Albums.objects.filter(title=title, artistid=artistid).exists():
            return Response(
                {"detail": "Album with this title and artist already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Albums.objects.all()
        title = self.request.query_params.get("title")
        if title is not None:
            queryset = queryset.filter(title=title)
            # Return only the first match if exists
            return queryset
        return queryset


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Tracks.objects.all()
    serializer_class = TrackSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlists.objects.all()
    serializer_class = PlaylistSerializer
