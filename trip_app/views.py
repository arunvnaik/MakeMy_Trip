from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from trip_app.models import Customer, Location, Cost
from trip_app.serializers import CustomerSerializer, LocationSerializer, CostSerializer
from trip_app.permission import AdminOrReadOnly
from trip_app.permission import IsAdminUser 
from rest_framework.permissions import IsAuthenticated





class CustomerListCreate(APIView):
    # permission_classes = [AdminOrReadOnly]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    permission_classes = [AdminOrReadOnly]
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return None
    
    def get(self, request, pk):
        customer = self.get_object(pk)
        if customer:
            serializer = CustomerSerializer(customer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        customer = self.get_object(pk)
        if customer:
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        customer = self.get_object(pk)
        if customer:
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)


# Create your views here.
class LocationListCreate(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetailView(APIView):
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            return None   
    
    def get(self, request, pk):
            location = self.get_object(pk)
            if location:
                serializer = LocationSerializer(location)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"detail": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
            location = self.get_object(pk)
            if location:
                serializer = LocationSerializer(location, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"detail": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
            location = self.get_object(pk)
            if location:
                location.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({"detail": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
        
class CostListCreate(APIView):
    def get(self, request):
        costs = Cost.objects.all()
        serializer = CostSerializer(costs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Cost.objects.get(pk=pk)
        except Cost.DoesNotExist:
            return None
    
    def get(self, request, pk):
        cost = self.get_object(pk)
        if cost:
            serializer = CostSerializer(cost)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Cost not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        cost = self.get_object(pk)
        if cost:
            serializer = CostSerializer(cost, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Cost not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        cost = self.get_object(pk)
        if cost:
            cost.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Cost not found"}, status=status.HTTP_404_NOT_FOUND)
    
    
