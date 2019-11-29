from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=30, unique=True)
    synonymous = models.ManyToManyField('self', blank=True,  related_name='synonymous')

    def __str__(self):
        return self.name


def adding_synonymous(synonymous):
    for word in synonymous:
        word.synonymous.set(synonymous.exclude(pk=word.pk))
