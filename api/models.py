from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class ManagementStaff(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='staff_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='staff_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"{self.name} {', '.join(self.groups.values_list('name', flat=True))}"
    

class Person(models.Model):
    GENDER = [
        ( 0, 'Male'),
        ( 1, 'Female'),
    ]

    name = models.CharField(max_length=100)
    gender = models.PositiveSmallIntegerField(choices=GENDER)
    age = models.PositiveSmallIntegerField()
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    
    class Meta:
        permissions = [
            ('full_access', 'Full Access'),
            ('assign_doctor', 'Assign Doctor'),
        ]

    def __str__(self):
        return f"{self.name} {self.phone_no}"
    
class Doctor(Person):
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.phone_no} {self.specialization}"

class Patient(Person):
    medical_history = models.TextField()
    assigned_doctor = models.ManyToManyField(Doctor, related_name='patients')