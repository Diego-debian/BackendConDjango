from django import forms
from django.forms import fields
from .models import *


""" Modelo para serializar el object como un form """
class objectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = '__all__'

""" Modelo para serializar el feed como un form """
class feedForm(forms.ModelForm):
    class Meta:
        model= Feed
        fields = '__all__'


""" Modelo para serializar el author como un form """
class authorForm(forms.ModelForm):
    class Meta:
        model= Author
        fields = '__all__'

""" Modelo para serializar el link como un form """
class linksForm(forms.ModelForm):
    class Meta:
        model= Links
        fields = '__all__'

""" Modelo para serializar el result como un form """
class resultForm(forms.ModelForm):
    class Meta:
        model= Results
        fields = '__all__'


""" Modelo para serializar el genre como un form """
class genreForm(forms.ModelForm):
    class Meta:
        model= Genres
        fields = '__all__'