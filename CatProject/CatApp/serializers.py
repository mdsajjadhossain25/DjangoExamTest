from rest_framework import serializers
from CatApp.models import CatShop

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatShop
        fields = '__all__'