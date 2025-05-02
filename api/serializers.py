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
    
class MappingSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField()
    doctor_id = serializers.IntegerField()

    class Meta:
        model = Patient
        fields = ['patient_id', 'doctor_id']

    def create(self, validated_data):
        patient = Patient.objects.get(id=validated_data['patient_id'])
        doctor = Doctor.objects.get(id=validated_data['doctor_id'])
        patient.assigned_doctor.add(doctor)
        return patient

    def to_representation(self, instance):
        return {
            "patient_id": instance.id,
            "name": instance.name,  # Assuming the Patient model has a 'name' field
            "assigned_doctors": [
                {"doctor_id": doctor.id, "name": doctor.name}
                for doctor in instance.assigned_doctor.all()
            ]
        }
        