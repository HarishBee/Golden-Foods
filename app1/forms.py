from django import forms
from app1.models import register as rg ,password as ps ,forget as fg

class regform(forms.ModelForm):
    class Meta:
        model= rg
        fields='__all__'
class passform(forms.ModelForm):
    class Meta:
        model= ps
        fields='__all__'
class forgetform(forms.ModelForm):
    class Meta:
        model=fg
        fields='__all__'