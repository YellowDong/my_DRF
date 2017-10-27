from my_app.models import IpoInfo
from rest_framework import serializers


class IpoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpoInfo
        fields = '__all__'