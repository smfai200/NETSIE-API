from django.template.defaultfilters import slugify

from Bridger.models import *
from api.Models.ModelManagers.GenericManager import *


class Story(models.Model):
    Story_Title = models.CharField(max_length=32)
    Story_slug = models.SlugField(max_length=32, default='', blank=True)
    Story_Description = models.CharField(max_length=32)
    Story_Category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    Story_Image = models.FileField(upload_to="static/uploads/")
    FK_User = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    IsActive = models.BooleanField(null=True, blank=True, default=True)
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
    objects = Generic_Manager()

    def __str__(self):
        return self.Story_Title

    @property
    def Seasons(self):
        from api.Models.Season import Season
        Comments_ = Season().__class__.objects.sort_ascending().filter(Fk_Story=self.id)
        if (len(Comments_) == 1):
            return [Comments_[0]]
        elif (len(Comments_) > 1):
            return Comments_
        else:
            return

    def save(self, *args, **kwargs):
        self.Story_slug = slugify(self.Story_Title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Stories'