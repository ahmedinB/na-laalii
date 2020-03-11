from django.forms import ModelForm
from .models import mtrlinfo,DEALER
class mtrlform(ModelForm):
    class Meta:
        model=mtrlinfo
        fields ='__all__'
class dealerform(ModelForm):
    class Meta:
        model=DEALER
        fields="__all__"