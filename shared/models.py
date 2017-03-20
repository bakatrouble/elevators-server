from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Client(models.Model):
    full_name = models.TextField(blank=True)
    short_name = models.CharField(max_length=256, blank=True)
    registration_address = models.TextField(blank=True)
    location_address = models.TextField(blank=True)
    phone = models.CharField(max_length=256, blank=True)
    inn = models.CharField(max_length=256, blank=True)
    kpp = models.CharField(max_length=256, blank=True)
    account_number = models.CharField(max_length=256, blank=True)
    bank = models.CharField(max_length=256, blank=True)
    bik = models.CharField(max_length=256, blank=True)
    ogrn = models.CharField(max_length=256, blank=True)
    person_name = models.CharField(max_length=256, blank=True)
    person_post = models.CharField(max_length=256, blank=True)  # должность

    def __str__(self):
        return self.short_name


class Specialist(models.Model):
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    first_name = models.CharField(max_length=128, verbose_name='Имя')
    patr_name = models.CharField(max_length=128, verbose_name='Отчество')

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.patr_name)

    class Meta:
        verbose_name = 'специалист'
        verbose_name_plural = 'специалисты'


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.group = User.SUPERVISOR_GROUP
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    SUPERVISOR_GROUP = 'supervisor'
    SECRETARY_GROUP = 'secretary'
    ACCOUNTING_GROUP = 'accounting'
    TESTING_GROUP = 'testing'

    GROUP_CHOICES = (
        (SUPERVISOR_GROUP, 'Супервизор'),
        (SECRETARY_GROUP, 'Секретарь-референт'),
        (ACCOUNTING_GROUP, 'Сметно-договорной отдел'),
        (TESTING_GROUP, 'Испытательный центр'),
    )

    username = models.CharField(max_length=256, unique=True, verbose_name='Имя пользователя')
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, verbose_name='Группа')

    is_active = True
    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username

    @property
    def is_admin(self):
        return self.group == User.SUPERVISOR_GROUP

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
