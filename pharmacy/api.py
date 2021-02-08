from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .serializers import MedicineDoseSerializer
from . models import MedicineDose


class MedicineDoseViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = MedicineDoseSerializer

    queryset = MedicineDose.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
