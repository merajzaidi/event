from django import forms
from main.models import contact,mehfildetail
class Nameform(forms.Form):
    your_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = contact
        fields = {'contacter'}

class details(forms.Form):
    nizamat = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
    nizamimag = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file col-md-2'}))
    sadarat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sadaratimag = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file col-md-2'}))

    class Meta:
        model = mehfildetail
        fields={'nizamat','nizamimage','sadarat','sadaratimag','mehfil'}