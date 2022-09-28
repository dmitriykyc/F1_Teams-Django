from rest_framework import serializers

from ..models import Commands

class CommandsListSerializer(serializers.ModelSerializer):
    '''Список комманд'''

    class Meta:
        model = Commands
        fields = ('name', 'description')