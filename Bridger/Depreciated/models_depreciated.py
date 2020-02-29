from django.db import models


# These are just basic models to get us working on the project
# Update the models as you like, and override 'save' method to apply constraints
# Let me know if anything needs clearing up

class Content(models.Model):
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    to_be_published_on = models.DateTimeField()
    youtube_id = models.CharField(max_length=50, null=False, blank=False)
    thumbnail_url = models.TextField(null=False, blank=False)
    is_premium = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    views_on_youtube = models.IntegerField(null=False)


class Comment(models.Model):
    comment = models.TextField(null=False, blank=False)
    content = models.ForeignKey('Content', null=False, blank=False, on_delete=models.DO_NOTHING, related_name='content')
    user = models.ForeignKey('auth.User', null=False, blank=False, related_name='posted_by',
                             on_delete=models.DO_NOTHING)
    replies = models.ForeignKey('Comment', null=True, related_name='replies_to_this_comment',
                                on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    transaction_done_by = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user')
    show_dp = models.BooleanField(default=True)
    dp_url = models.TextField(null=True, blank=True)
    display_name = models.CharField(max_length=50, null=False, blank=False)
    is_premium = models.BooleanField(default=False)
