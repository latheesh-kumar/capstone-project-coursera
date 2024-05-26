from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu,Booking
from .serializers import MenuItemSerializer,BookingItemSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])

def msg(request):
    return HttpResponse({"message":"This view is protected"})

def index(request):
    return render(request, 'index.html',{})


# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingItemSerializer

class SingleBookingItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingItemSerializer