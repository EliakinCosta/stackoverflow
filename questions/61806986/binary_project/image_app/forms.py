from django import forms
from django.forms import formset_factory
from . import models


class ThermalSourceForm(forms.ModelForm):

    scheme_image = forms.FileField(required=False)

    def save(self, commit=True):
        if self.cleaned_data.get('scheme_image') is not None \
                and hasattr(self.cleaned_data['scheme_image'], 'file'):
            data = self.cleaned_data['scheme_image'].file.read()
            self.instance.scheme_image = data
        return self.instance

    def save_m2m(self):
        # FIXME: this function is required by ModelAdmin, otherwise save process will fail
        pass

    class Meta:
        model = models.Word
        fields = ['name', 'scheme_image']


class InsereIdioma(forms.ModelForm):
    class Meta:
        model = models.Idioma
        fields = '__all__'
        exclude = ['usuario']
InsereIdiomaFormset = formset_factory(InsereIdioma, extra=1)

class InsereTecnologia(forms.ModelForm):
    class Meta:
        model = models.Tecnologia
        fields = '__all__'
        exclude = ['usuario']
InsereTecnologiaFormset = formset_factory(InsereTecnologia, extra=1)


class K8Points_ClassroomForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(K8Points_ClassroomForm, self).clean()

        day = cleaned_data.get("day")
        time_frame = cleaned_data.get("time_frame")
        student_name = cleaned_data.get("student_name")

        if models.K8Points.objects.filter(day=day, time_frame=time_frame, student_name=student_name).exists():
            raise forms.ValidationError(
                'This timeframe {} was already logged to the student {} on {}'.format(time_frame, student_name.student_name, day)
            )

    class Meta:
        model = models.K8Points
        fields = ('student_name', 'behavior','academic', 'time_frame','date','day','week_of','class_name')


class K8PointsForm(forms.ModelForm):

    class Meta:
        model = models.K8Points
        fields = ('student_name', 'behavior','academic', 'time_frame','date','day','week_of','class_name')


def cities_as_choices():
    choices = []
    for country in models.Cities.objects.values('country').distinct():
        new_country = []
        cities = []
        new_country.append(country.get('country'))

        for city in models.Cities.objects.filter(country=country.get('country')):
            cities.append([city.pk, city.city])

        new_country.append(cities)
        choices.append(new_country)

    return choices


class CityNameForm(forms.Form):
    """
    CityNameForm Class
    """

    def __init__(self, *args, **kwargs):
        super(CityNameForm, self).__init__(*args, **kwargs)
        self.fields['cityName'].choices = cities_as_choices()

    cityName = forms.ChoiceField(
        choices=cities_as_choices(),
        help_text="",
        required=False,
        label='Cities',
    )


class QuoteForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = models.Quote
        fields = ['name',]
