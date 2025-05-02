from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import exceptions as rest

from .serializers import *


@api_view(['POST'])
@permission_classes([AllowAny])
def auth(request, action):
    if action == 'register':
        serializer = ManagementStaffSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
        

    
