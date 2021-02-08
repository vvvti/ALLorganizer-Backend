from rest_framework import serializers
from . models import MedicineDose


class MedicineDoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineDose
        fields = (
            '__all__'
        )