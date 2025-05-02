from rest_framework import serializers
from .models import ManagementStaff, Patient, Doctor


class ManagementStaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = ManagementStaff
        fields = ['email', 'name', 'password']

    def create(self, validated_data):
        user = ManagementStaff.objects.create_user(**validated_data)
        return user
    
class PatientSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Patient
        fields = ['id', 'name', 'gender', 'age', 'phone_no', 'address', 'medical_history']

    def create(self, validated_data):
        return super().create(validated_data)
    

class DoctorSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'gender', 'age', 'phone_no', 'address', 'specialization']

    def create(self, validated_data):
        return super().create(validated_data)