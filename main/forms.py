from django import forms
from main.models import contact,mehfildetail,User,postrequest
from django.contrib.auth.forms import ReadOnlyPasswordHashField

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
    nizamimag = forms.FileField(label='Avatarr', required=True, error_messages={'invalid':"Images only"}, widget=forms.FileInput)
    #nizamimag = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file col-md-2'}))
    sadarat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sadaratimag = forms.FileField(label='Avatar', required=True, error_messages={'invalid':"Images only"}, widget=forms.FileInput)
    #sadaratimag = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file col-md-2'}))

    class Meta:
        model = mehfildetail
        exclude=('mehfil',)
class mehfilform(forms.Form):
    class Meta:
        model = postrequest

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(label= 'Confirm password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =('email','full_name',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password Don't Match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email','full_name',)
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password doesn't match")
        return password2
    def save(self, commit=True):
        user  = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ('full_name','email','password','active','superuser')

    def clean_password(self):
        return self.initial["password"]
