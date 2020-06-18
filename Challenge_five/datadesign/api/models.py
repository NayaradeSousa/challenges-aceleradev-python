from django.db import models
from django.core import validators


def validation_log_levels(level):
    if level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        raise validators.ValidationError('Level is wrong!')


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    last_login = models.DateTimeField('Last Login', auto_now=True)
    email = models.EmailField(
        'E-mail',
        validators=[validators.validate_email]
    )
    password = models.CharField(
        'Password',
        max_length=50,
        validators=[validators.MinValueValidator(8)]
    )

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField('Name', max_length=50)
    status = models.BooleanField()
    env = models.CharField('Env', max_length=20)
    version = models.CharField('Version', max_length=5)
    address = models.CharField(
        'Address',
        max_length=39,
        validators=[validators.validate_ipv4_address]
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    level = models.CharField(
        'Level',
        max_length=20,
        validators=[validation_log_levels]
    )
    data = models.TextField('Data')
    arquivado = models.BooleanField('Filed')
    date = models.DateField('Date', auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.level


class Group(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
