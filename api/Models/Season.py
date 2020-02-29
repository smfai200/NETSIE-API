from django.template.defaultfilters import slugify

from Bridger.models import *
from api.Models.ModelManagers.GenericManager import *


class Season(models.Model):
    Season_Title = models.CharField(max_length=32)
    Season_slug = models.SlugField(max_length=32, default='', blank=True)
    Season_Image = models.FileField(upload_to="static/uploads/", blank= True, null=True)
    Fk_Story = models.ForeignKey(Story, on_delete=models.DO_NOTHING)
    IsActive = models.BooleanField(default=True)
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
    objects = Generic_Manager()

    def __str__(self):
        return self.Season_Title

    @property
    def Episodes(self):
        from api.Models.Episode import Episode
        Comments_ = Episode().__class__.objects.sort_ascending().filter(Episode_Season=self.id)
        if (len(Comments_) == 1):
            return [Comments_[0]]
        elif (len(Comments_) > 1):
            return Comments_
        else:
            return

    def save(self, *args, **kwargs):
        self.Season_slug = slugify(self.Season_Title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Seasons'