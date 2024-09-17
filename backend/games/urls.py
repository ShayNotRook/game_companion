from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .api.v1.api_views import GameViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet, basename='games')

urlpatterns = [
    path('api/v1/', include(router.urls))
]