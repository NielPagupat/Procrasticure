from rest_framework import serializers
from .models import productivityTimer

class createTaskTimer(serializers.ModelSerializer):
    class Meta:
        model = productivityTimer
        fields = '__all__'