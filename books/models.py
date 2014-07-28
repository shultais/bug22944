from django.db import models


class Book(models.Model):
    title = models.CharField(u"Title", max_length=100)

    class Meta:
        verbose_name = u"book"
        verbose_name_plural = u"books"
        ordering = ["title"]

    def __unicode__(self):
        return self.title