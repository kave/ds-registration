from django.db import models
from datetime import datetime

class Registration(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=True)
    phone = models.TextField(max_length=15, blank=True)
    can_model = models.BooleanField(default=False, blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def get_name(self):
        return self.first_name + ' ' + self.last_name
    get_name.short_description = 'Name'

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = "DeepScrub Registration"
        verbose_name_plural = "DeepScrub Registration"
