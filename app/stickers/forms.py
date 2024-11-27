from django import forms

from .models import Sticker

class StickerForm(forms.ModelForm):

    class Meta:
        model = Sticker
        fields = ("sticker", "expires", "name", "no_plate", "model")
        widgets = {
            "expires": forms.DateInput(attrs={"type": "date"}),
        }