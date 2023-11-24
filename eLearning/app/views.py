from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InteractionHistoryViewSet(viewsets.ModelViewSet):
    queryset = InteractionHistory.objects.all()
    serializer_class = InteractionHistorySerializer


class InteractionHistoryViewSet(viewsets.ModelViewSet):
    queryset = InteractionHistory.objects.all()
    serializer_class = InteractionHistorySerializer


class InteractionHistoryViewSet(viewsets.ModelViewSet):
    queryset = InteractionHistory.objects.all()
    serializer_class = InteractionHistorySerializer


class InteractionHistoryViewSet(viewsets.ModelViewSet):
    queryset = InteractionHistory.objects.all()
    serializer_class = InteractionHistorySerializer


class InteractionHistoryViewSet(viewsets.ModelViewSet):
    queryset = InteractionHistory.objects.all()
    serializer_class = InteractionHistorySerializer
