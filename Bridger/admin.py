from django.apps import apps
from django.contrib import admin

models = ["Category","Story","Season","Episode","EpisodeReview"]

for model in models:
    admin.site.register(apps.get_model("api."+model))