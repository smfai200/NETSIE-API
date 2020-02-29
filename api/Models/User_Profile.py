from api.Models.ModelManagers.GenericManager import *

class UserProfile(models.Model):
    UserProfile_User = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    User_FullName = models.CharField(max_length=250, blank=True, null=True)
    User_photo = models.FileField(upload_to="static/uploads/", blank=True, null=True)
    User_Bio = models.CharField(max_length=250, blank=True, null=True)
    User_Country = models.CharField(max_length=250)
    IsActive = models.BooleanField(default=True)
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
    objects = Generic_Manager()

    def __str__(self):
        return self.User_FullName

    @property
    def Favourites(self):
        Comments_ = UserFavourite().__class__.objects.sort_ascending().filter(UserFavourite_User=self.id)
        if (len(Comments_) == 1):
            return [Comments_[0]]
        elif (len(Comments_) > 1):
            return Comments_
        else:
            return

    class Meta:
        verbose_name_plural = 'Users'

class UserFavourite(models.Model):
    User_fk = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    Story = models.CharField(max_length=250, blank=True, null=True)
    Season = models.FileField(upload_to="static/uploads/", blank=True, null=True)
    Episode = models.CharField(max_length=250, blank=True, null=True)
    IsActive = models.BooleanField(default=True)
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
    objects = Generic_Manager()

    def __str__(self):
        return self.UserProfile_User

    class Meta:
        verbose_name_plural = 'UserFavourites'
