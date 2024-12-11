from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from .forms import ImageCreateForm
from django.shortcuts import get_object_or_404
from .models import Image
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from images.models import Image

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            new_image = form.instance
            new_image.user = request.user
            new_image.save()
            messages.success(request,
                             'Изображения успешно добавлено')
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                  'form': form})

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image})

"""def image_loading(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfiles1']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        return render(request,
                      'images/image/create.html',
                      {'file_url': file_url})"""

@login_required
def image_list(request):
    images = Image.objects.all()

    return render(request,
            'images/image/list_images.html',
            {'section': 'images',
            "images": images})

@login_required
def image_list2(request):
    images = Image.objects.all()

    return render(request,
            'images/image/list_images2.html',
            {'section': 'images',
            "images": images})

