from django import forms
from webapp.models import Product

class ProductForm(forms.ModelForm):
    remainder = forms.IntegerField(min_value=0)
    cost = forms.DecimalField(max_digits=7, decimal_places=2)
    image = forms.ImageField()
    class Meta:
        model = Product
        fields = ('title', 'text', 'image', 'category', 'remainder', 'cost')