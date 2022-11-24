from rest_framework import serializers
from .models import Realtor


class RealtorSeriazizer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'
