# urls.py

from django.urls import path,include 
from trip_app.views  import (CustomerListCreate,CustomerDetailView,LocationListCreate,LocationDetailView,
                             CostListCreate,CostDetailView)

urlpatterns = [
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/',CustomerDetailView.as_view(),name ='customer-detail'),
    path('locations/', LocationListCreate.as_view(), name='location-list-create'),
    path('locations/<int:pk>/',LocationDetailView.as_view(),name ='location-detail'),
    path('costs/', CostListCreate.as_view(), name='cost-list-create'),
    path('costs/<int:pk>/',CostDetailView.as_view(),name ='cost-detail'),
    
    
]
