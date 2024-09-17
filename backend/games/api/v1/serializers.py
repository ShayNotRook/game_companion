from rest_framework import serializers

from games.models import Game

class GameSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    cover_url = serializers.SerializerMethodField()
    class Meta:
        model = Game
        fields = ["id" ,"title", "genres", "cover_url", "publisher", "developer"]
        
    def get_cover_url(self, obj):
        request = self.context.get('request')
        if obj.cover and hasattr(obj.cover, 'url'):
            return request.build_absolute_uri(obj.cover.url)
        return None
