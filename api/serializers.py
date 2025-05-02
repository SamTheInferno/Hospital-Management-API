from rest_framework import serializers
from .models import ManagementStaff


class ManagementStaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = ManagementStaff
        fields = ['email', 'name', 'password']

    def create(self, validated_data):
        user = ManagementStaff.objects.create_user(**validated_data)
        return user