from django.template.defaultfilters import slugify

from api.Models.ModelManagers.GenericManager import *


class Category(models.Model):
    Category_Title = models.CharField(max_length=64)
    Category_Image = models.FileField(upload_to="static/uploads/")
    Category_slug = models.SlugField(max_length=32, default='', blank=True)
    IsActive = models.BooleanField(default=True)
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
    objects = Generic_Manager()

    def __str__(self):
        return self.Category_Title

    def save(self, *args, **kwargs):
        self.Category_slug = slugify(self.Category_Title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'