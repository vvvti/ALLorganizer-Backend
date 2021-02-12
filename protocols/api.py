from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .serializers import ProtocolSerializer
from . models import Protocol


class ProtocolViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ProtocolSerializer

    queryset = Protocol.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
