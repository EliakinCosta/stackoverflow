from __future__ import unicode_literals
import django_filters
from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="phone number must be entered in the format: '+2340000000000'. Up to 15 digits allowed.")

@python_2_unicode_compatible
class Employee(models.Model):
    # basic information of employee
    first_name = models.CharField(_('first name'), max_length=40)
    last_name = models.CharField(_('last name'), max_length=40)
    emp_photo = models.ImageField(_('passport'))
    date_of_birth = models.DateField(_('birthday'))
    house_address = models.CharField(_('house address'), max_length=50)
    city_of_residence = models.CharField(_('city'), max_length=40)
    local_govt_of_origin = models.CharField(_('LGA of origin'), max_length=40)
    town_or_city_of_origin = models.CharField(_('town or city'), max_length=40)
    email = models.EmailField(_("email address"))
    phone_number = models.CharField(_('phone number'), validators=[phone_regex], max_length=17, blank=True)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
