from django.db import models
from django.urls import reverse


class Feed(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    def __str__(self):
        return "{} ({})".format(self.title, self.url)

    def get_abosulute_url(self):
        return reverse('feed:feed_list_detail', kwargs={'feed_id': self.id})
