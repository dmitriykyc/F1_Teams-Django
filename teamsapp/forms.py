from django import forms

from .models import Rewiews

class ReviewFrorm(forms.ModelForm):
    """ Форма для отзывов """
    class Meta:
        model = Rewiews
        fields = ('name', 'text', 'email')