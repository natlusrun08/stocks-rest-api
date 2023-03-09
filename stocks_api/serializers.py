from rest_framework import serializers
from .models import InstitutionalHolder

class InstitutionalHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionalHolder
        fields = ['id', 'name', 'shares_held', 'percentage_held']
