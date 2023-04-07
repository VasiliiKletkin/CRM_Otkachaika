from dal import autocomplete
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class ProfileInlineForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
        widgets = {
            'company': autocomplete.ModelSelect2(url='company-autocomplete', attrs={'data-minimum-input-length': 3}),
        }
