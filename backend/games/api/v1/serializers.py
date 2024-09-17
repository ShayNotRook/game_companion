from rest_framework import serializers

from games.models import Game

class GameSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Game
        fields = ["title", "genres", "cover", "publisher", "developer"]
