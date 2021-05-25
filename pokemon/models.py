from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    base_hp = models.FloatField(blank=True, null=True)
    base_attack = models.FloatField(blank=True, null=True)
    base_defense = models.FloatField(blank=True, null=True)
    base_special_attack = models.FloatField(blank=True, null=True)
    base_special_defense = models.FloatField(blank=True, null=True)
    base_speed = models.FloatField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')


class Evolutions(models.Model):
    preevolution = models.ForeignKey(
        Pokemon,
        related_name='is_preevolution_of',
        on_delete=models.PROTECT)

    evolution = models.ForeignKey(
        Pokemon,
        related_name='is_evolution_of',
        on_delete=models.PROTECT)

    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
