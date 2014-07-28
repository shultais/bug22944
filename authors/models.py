from django.db import models


class Author(models.Model):
    name = models.CharField(u"Name", max_length=100)

    class Meta:
        verbose_name = u"author"
        verbose_name_plural = u"authors"
        ordering = ["name"]

    def __unicode__(self):
        return self.name