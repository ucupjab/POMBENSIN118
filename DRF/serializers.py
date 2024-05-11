from rest_framework import serializers
from .models import PomBensin, Pembeli

class PomBessinSerializer(serializers.ModelSerializer):
Pembeli = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = PomBensin
        fields = ["id", "nama", "pombensin"]

class PembeliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembeli
        fields = ["id", "nama", "pembeli"]