from __future__ import unicode_literals

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class AccountUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class AccountUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='first name', max_length=255, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=255, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_staff = models.BooleanField(
            verbose_name='staff status',
            default=False,
    )
    is_active = models.BooleanField(
            verbose_name='active',
            default=True,
            help_text=('Designates whether this user should be treated as active. '
                       'Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(verbose_name='date joined', default=timezone.now)

    objects = AccountUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns first_name as short name
        """
        return self.first_name
