from django.db import models

class Generic_QuerySet(models.QuerySet):
    def all_active(self):
        return self.filter(IsActive=True)

    def sort_ascending(self):
        return self.all_active().order_by("-CreateDate")

    def sort_descending(self, size):
        return self.all_active().order_by("CreateDate")

class Generic_Manager(models.Manager):
    def get_queryset(self):
        return Generic_QuerySet(self.model, using=self._db).filter(IsActive=True)

    def sort_ascending(self):
        return self.get_queryset().sort_ascending()

    def sort_descending(self, size):
        return self.get_queryset().sort_descending(size)

    def all_active(self):
        return self.get_queryset().all_active()


