from django import forms
from django.forms import fields
from .models import Page,Carousel

class CarouselModelForm(forms.ModelForm):
    class Meta:
        model = Carousel
        # fields = '__all__'
        fields = [
            'title',
            'cover_image',
            'status',
        ]
        

class PageModelForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'title',
            'cover_image',
            'content',
            'status',
        ]