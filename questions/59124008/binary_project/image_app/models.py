from django.db import models
from django.utils.safestring import mark_safe


class Word(models.Model):
    name = models.CharField(max_length=30, unique=True)
    scheme_image = models.BinaryField(verbose_name='Scheme', blank=True, null=True, editable=True)

    def scheme_image_tag(self):
        from base64 import b64encode
        return mark_safe('<img src = "data: image/png; base64, {}" width="200" height="100">'.format(
            b64encode(self.scheme_image).decode('utf8')
        ))

    scheme_image_tag.short_description = 'Image'
    scheme_image_tag.allow_tags = True

    def __str__(self):
        return self.name
