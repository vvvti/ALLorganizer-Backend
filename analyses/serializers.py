from rest_framework import serializers
from . models import CrpAnalysis, CompleteBloodCount, ALT_AST, UrineAnalisis


class CrpAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrpAnalysis
        fields = (
            '__all__'
        )

class CompleteBloodCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompleteBloodCount
        fields = (
            '__all__'
        )

class ALT_ASTSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALT_AST
        fields = (
            '__all__'
        )
class UrineAnalisisSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrineAnalisis
        fields = (
            '__all__'
        )
