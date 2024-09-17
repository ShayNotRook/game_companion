from rest_framework import viewsets, status
from rest_framework.response import Response

from games.models import Game

from .serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    
    def list(self, request, *args, **kwargs):
        try:
            games = self.get_queryset()
            serializer = self.get_serializer(games, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    