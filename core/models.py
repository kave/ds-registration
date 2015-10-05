from django.db import models


class Registration(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    phone = models.TextField(max_length=15, blank=False)
    can_model = models.BooleanField(blank=False)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = "DeepScrub Registration"
        verbose_name_plural = "DeepScrub Registration"
