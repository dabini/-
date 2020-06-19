from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'age', 'gender']
        widgets = {
               'gender': forms.RadioSelect(choices=GENDER_CHOICES)
           }