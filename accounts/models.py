from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from hospitals.models import Hospital

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, phone, password, **extra_fields):
        values = [email, name, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, phone, password, **extra_fields)

    def create_superuser(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, name, phone, password, **extra_fields)


class Doctor(AbstractBaseUser, PermissionsMixin):
	picture = models.ImageField(default = 'Avatar.png',upload_to = 'users/' ,blank = True, null = True)
	email = models.EmailField(unique = True)
	name = models.CharField(max_length = 150)
	lastname = models.CharField(max_length = 150)
	phone = models.CharField(max_length = 50)
	working_place = models.ForeignKey(Hospital, on_delete = models.CASCADE, null = True)
	role = models.CharField(max_length = 50)
	is_accept = models.BooleanField(default = False)



	is_staff = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)
	date_joined = models.DateTimeField(default = timezone.now)
	last_login = models.DateTimeField(null = True)


	objects = AccountManager()


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name', 'phone']


	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.name.split()[0]
