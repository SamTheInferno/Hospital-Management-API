from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import ManagementStaff
from rest_framework_simplejwt.exceptions import InvalidToken

class ManagementStaffJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']
        except KeyError:
            raise InvalidToken('Token contained no recognizable user identification')

        try:
            return ManagementStaff.objects.get(id=user_id)
        except ManagementStaff.DoesNotExist:
            raise InvalidToken('User not found')
