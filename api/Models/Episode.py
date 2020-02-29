from django.template.defaultfilters import slugify

from Bridger.models import *
from api.Models.ModelManagers.GenericManager import *


class Episode(models.Model):
    Episode_Title = models.CharField(max_length=32)
    Episode_slug = models.SlugField(max_length=32, default='', blank=True)
    Episode_TextStory = models.CharField(max_length=8000)
    Episode_Image = models.FileField(upload_to="static/uploads/", blank= True, null=True)
    Episode_Season = models.ForeignKey(Season, on_delete=models.DO_NOTHING)
    IsActive = models.BooleanField(default=True)
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
    objects = Generic_Manager()

    def __str__(self):
        return self.Episode_Title

    def save(self, *args, **kwargs):
        self.Episode_slug = slugify(self.Episode_Title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Episodes'