from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import exceptions as rest
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *
from .permissions import *


@api_view(['POST'])
@permission_classes([AllowAny])
def auth(request, action):
    if action == 'register':
        serializer = ManagementStaffSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
    elif action == 'login':
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = ManagementStaff.objects.filter(email=email).first()
        if not user:
            raise rest.AuthenticationFailed('Invalid User')
        if not user.check_password(password):
            raise rest.AuthenticationFailed('Invalid Password')
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token), **ManagementStaffSerializer(user).data}, status=200)

# @api_view(['POST', 'GET'])
# @permission_classes([IsOfficer])    
class AddPatient(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsOfficer]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def post(self, request):   
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)
    
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)        
        return Response(serializer.data, status=201)

class ModifyPatient(APIView):
    def get(self, request, id):
        patient = Patient.objects.get(id=id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=200)
    
    def put(self, request, id):
        patient = Patient.objects.get(id=id)
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    
    def delete(self, request, id):
        patient = Patient.objects.get(id=id)
        patient.delete()
        return Response(status=204)
    
class AddDoctor(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsOfficer]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def post(self, request):   
        serializer = DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)
    
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)        
        return Response(serializer.data, status=200)

class ModifyDoctor(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        doctor = Doctor.objects.get(id=id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=200)
    
    def put(self, request, id):
        doctor = Doctor.objects.get(id=id)
        serializer = DoctorSerializer(doctor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    
    def delete(self, request, id):
        doctor = Doctor.objects.get(id=id)
        doctor.delete()
        return Response(status=204)

