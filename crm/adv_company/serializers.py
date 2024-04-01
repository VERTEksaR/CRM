from rest_framework import serializers

from .models import AdvCompany


class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvCompany
        depth = 1
        fields = '__all__'
