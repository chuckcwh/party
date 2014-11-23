import user
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from partyApp.models import Profile, Party


class ProfileForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

class UserEditForm(UserChangeForm):
    sex_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    first_name = forms.CharField(help_text="First Name")
    last_name = forms.CharField(help_text="Last Name")
    email = forms.EmailField(help_text="abc@gmail.com")
    birth = forms.DateField(help_text="1992-08-10")
    sex = forms.ChoiceField(choices=sex_choice)
    about = forms.CharField(help_text="Tell people something about you!")

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'birth', 'sex', 'about', 'password')

class UserImageForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)

# If you made this a ModelForm instead of a regualr form, you wouldn't have to define all of the fields
class PartyForm(forms.Form):
    sex_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    title = forms.CharField(required=True, help_text='required')
    latitude = forms.FloatField(required=True, help_text='required')
    longitude = forms.FloatField(required=True, help_text='required')
    time = forms.DateTimeField(help_text='Ex. 2014-08-01 15:26')
    maxPpl = forms.IntegerField()
    minAge = forms.IntegerField()
    maxAge = forms.IntegerField()
    targetSex = forms.ChoiceField(choices=sex_choice)

    class Meta:
        model = Party
        field = ('title', 'latitude', 'longitude', 'time', 'maxPpl', 'minPpl', 'minAge', 'maxAge', 'targetSex')
