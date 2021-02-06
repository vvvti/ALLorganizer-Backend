from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .serializers import CrpAnalysisSerializer, CompleteBloodCountSerializer, ALT_ASTSerializer, UrineAnalisisSerializer
from . models import CrpAnalysis, CompleteBloodCount, ALT_AST, UrineAnalisis


class CrpAnalysisViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = CrpAnalysisSerializer

    queryset = CrpAnalysis.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CompleteBloodCountViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = CompleteBloodCountSerializer

    def get_queryset(self):
        return self.request.user.completebloodcount.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ALT_ASTViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ALT_ASTSerializer

    def get_queryset(self):
        return self.request.user.alt_ast.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UrineAnalisisViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UrineAnalisisSerializer

    def get_queryset(self):
        return self.request.user.UrineAnalisisViewSet.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
