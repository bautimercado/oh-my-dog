from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
#from perros.models import Perro

# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, error_messages={
            'unique': 'Ya existe un usuario con este email'})
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=30, unique=True, error_messages= {
            'unique': 'Ya existe un usuario con este DNI'})
    telefono = models.CharField(max_length=30, unique=True, error_messages={
            'unique': 'Ya existe un usuario con este telefono'})
    activo = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def get_nombre(self):
        return self.nombre
    
    def get_activo(self):
        return self.activo
    

        