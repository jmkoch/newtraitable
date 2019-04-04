from django import forms
from .models import Trait, Pub

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

class PubForm(forms.ModelForm):
	class Meta:
		model = Pub
		exclude = [id, ]
	def clean(self):
		title = self.cleaned_data.get('title')
		lastName = self.cleaned_data.get('lastName')
		middleName = self.cleaned_data.get('middleName')
		firstName = self.cleaned_data.get('firstName')
		citekey = self.cleaned_data.get('citekey')
		pub_type = self.cleaned_data.get('pub_type')