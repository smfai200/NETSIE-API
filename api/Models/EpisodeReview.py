from Bridger.models import *
from api.Models.ModelManagers.GenericManager import *

class EpisodeReview(models.Model):
    EpisodeReview_Rating = models.IntegerField()
    EpisodeReview_Comment = models.CharField(max_length=1000)
    EpisodeReview_slug = models.SlugField(max_length=32, default='', blank=True)
    EpisodeReview_Episode = models.ForeignKey(Episode, on_delete=models.DO_NOTHING)
    EpisodeReview_User = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    IsActive = models.BooleanField(default=True)
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
    objects = Generic_Manager()

    class Meta:
        verbose_name_plural = 'EpisodeReviews'