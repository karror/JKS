from django.db import models


class Cont(models.Model):
    short_description = 'cont'
    name = models.CharField(
        'nazwa',
        max_length=20,
        null=True,
        blank=True)
    description = models.TextField(
        'podpis',
        null=True,
        blank=True)
    mail_text = models.TextField(
        'treść wiadomości',
        null=True,
        blank=True)
    link = models.URLField(
        'link',
        max_length=200,
        null=True,
        blank=True)
    photer = models.ForeignKey('Photer', models.SET_NULL, null=True, blank=True)


class Photer(models.Model):
    short_description = 'photer'
    main = models.ImageField(
        'main',
        null=True,
        blank=True)
    tlow = models.ImageField(
        'tlow',
        null=True,
        blank=True)
    thigh = models.ImageField(
        'thigh',
        null=True,
        blank=True)
    mail = models.ImageField(
        'mail',
        null=True,
        blank=True)

