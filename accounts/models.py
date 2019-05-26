from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#from django.contrib.auth import get_user_model

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            name= name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class User (AbstractBaseUser,PermissionsMixin):
    username = models.CharField('Usuário', max_length=30, unique= True)
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', blank=True, max_length=100)
    is_staff = models.BooleanField('É Líder do Grupo?', blank=True, default=False)
    date_joined = models.DateTimeField('Data Cadastro', auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name']

    objects = MyUserManager()
    
    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)


    class Meta:
        verbose_name='Usuário'
        verbose_name_plural='Usuários'
        

