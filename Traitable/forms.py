from django import forms
from Traitable.models import Trait

#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Submit

class TraitForm(forms.ModelForm):
    class Meta:
        model = Trait
        exclude = [id, ]
    def clean(self):
        genus = self.cleaned_data.get('genus')
        species = self.cleaned_data.get('species')
        isi = self.cleaned_data.get('isi')
        fruit_type = self.cleaned_data.get('fruit_type')
        if isi > 1.0:
            raise forms.ValidationError("ISI must be between 0.0 and 1.0")
        return self.cleaned_data
