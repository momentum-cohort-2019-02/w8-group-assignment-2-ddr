from django import forms
from core.models import Deck


class DeckForm(forms.ModelForm):

    class Meta:
        model = Deck
        fields = ("name",)
