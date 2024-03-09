from rest_framework import serializers
from trip_app.models import Customer, Location, Cost

class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    # costs = CostSerializer(many=True, read_only=True)  # Nested relationship with Cost
    cost = CostSerializer(read_only=True) 

    class Meta:
        model = Location
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)  # Nested relationship with Location

    class Meta:
        model = Customer
        fields = '__all__'


