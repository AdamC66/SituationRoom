from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import permissions


class HeartBeatViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        return Response("Thump")
