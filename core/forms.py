from django.forms import ModelForm, PasswordInput
from core.models import Campus

class CampusForm(ModelForm):
    class Meta:
        model = Campus
        fields = '__all__'

