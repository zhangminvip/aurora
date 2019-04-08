from django.shortcuts import render
from django.contrib.auth.models  import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, PermissionSerializer
from django.contrib.auth.models import Permission

# Create your views here.

class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
