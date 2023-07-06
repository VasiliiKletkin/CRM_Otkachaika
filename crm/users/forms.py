from dal import autocomplete
from django import forms

from .models import Profile


class ProfileInlineForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            "company": autocomplete.ModelSelect2(url="company-autocomplete"),
            "telegram": autocomplete.ModelSelect2(url="telegram-autocomplete"),
        }
