from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.models import Permission

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission

class  UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # field = ('url', 'username', 'email', 'groups')
        fields = '__all__'
        # exclude = ('user_permissions',)
        # lookup_field = 'username'



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        # field = ('url', 'name')

        # exclude = ('group_permissions',)
        fields = '__all__'
        # lookup_field = 'name'
