from rest_framework import serializers

from bowling.models import Booking, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class BowlingSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ['id', 'date', 'client']