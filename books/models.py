from django.db import models
from authors.models import Author


class Book(models.Model):
    author = models.ForeignKey(Author, verbose_name=u"author", default=None, blank=True, null=True)
    title = models.CharField(u"Title", max_length=100)

    class Meta:
        verbose_name = u"book"
        verbose_name_plural = u"books"
        ordering = ["title"]

    def __unicode__(self):
        return self.title