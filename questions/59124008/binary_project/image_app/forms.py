from django import forms
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
