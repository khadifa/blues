'''from django import forms
from .models import Products

class Products(forms.ModelForm):
    PortName = forms.CharField(required=True,widget=forms.TextInput(attrs={
        "placeholder":"PortName",
    }))
    Contact = forms.CharField(required=True,widget=forms.TextInput(attrs={
        "placeholder":"Contact",
        
    }))
    Location = forms.CharField(required=True,widget=forms.TextInput(attrs={
        "placeholder":"Location",
        
    }))
    Status = forms.CharField(required=True,widget=forms.TextInput(attrs={
        "placeholder":"Status",
        
    }))
    class Meta:
        model = Products
        fields = ('PortName','Contact','Location','Status')'''





