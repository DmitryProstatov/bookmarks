from http.client import responses

from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests
from django import forms
from requests import request

from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'image']
        #widgets = {'url': forms.HiddenInput,}

    def clean_url(self):
        url = self.cleaned_data['title']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Указанный URL-адрес не соответсвует расширениям изображений')
        return url

    '''def save(self, force_insert=False,
             force_update=False,
             commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['title']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}{extension}'
        response = request.get(image_url)
        image.image.save(image_name,
                         ContentFile(response.content),
                         save=False)
        if commit:
            image.save()
        return image'''

    #file = forms.FileField()



