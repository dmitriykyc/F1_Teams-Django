from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Commands
from .serializers import CommandsListSerializer


class CommandsListView(APIView):

    def get(self, request):
        commands = Commands.objects.all()
        serializer = CommandsListSerializer(commands, many=True)
        return Response(serializer.data)
