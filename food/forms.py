from .models import Items
from django import forms

class itemForm(forms.ModelForm):
    """Form definition for itemForm."""

    class Meta:
        """Meta definition for itemForm."""

        model = Items
        fields = ('item_name', 'item_desc', 'item_price', 'item_img')
