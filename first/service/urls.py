from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, ArtistViewSet, TrackViewSet, PlaylistViewSet

router = DefaultRouter()
router.register(r"albums", AlbumViewSet)
router.register(r"artists", ArtistViewSet)
router.register(r"tracks", TrackViewSet)
router.register(r"playlists", PlaylistViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
