from django import forms
from BastianWorld.models import Album, Services, Qualifications, Contakt, Start


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    zip = forms.FileField(required=False)

class ServicesForm(forms.ModelForm):

    class Meta:
        model = Services
        exclude = ['title', 'description', 'photo']


class QualForm(forms.ModelForm):

    class Meta:
        model = Qualifications
        fields = ['title', 'description', 'photo']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contakt
        exclude = ['Nazwa', 'NrTel', 'Email','GitHub', 'LinkedIn', 'Facebook']


class StartForm(forms.ModelForm):
    class Meta:
        model = Start
        exclude = ['title', 'description']