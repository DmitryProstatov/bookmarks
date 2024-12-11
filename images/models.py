

from django.core.files.uploadedfile import UploadedFile
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse
from easy_thumbnails.fields import ThumbnailerImageField


class Image(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000, blank=True)
    #image = models.ImageField(upload_to='images/%Y/%m/%d')
    image = ThumbnailerImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id,
                                              self.slug])

