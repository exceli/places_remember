from allauth.socialaccount.models import SocialAccount
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from pytils.translit import slugify
from django_ymap.fields import YmapCoord


class Place(models.Model):
    auth = models.ForeignKey(SocialAccount, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Author'))
    address = YmapCoord(max_length=200, start_query=u'Россия', size_width=500, size_height=500, verbose_name=_('Address'))
    title = models.CharField(max_length=150, db_index=True, verbose_name=_('Title'))
    review = models.CharField(max_length=10000, verbose_name=_('Remember'))
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, verbose_name=_('Date of create'))
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL', blank=True, null=True)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'detail_slug': self.slug})

    def get_trim_review(self):
        return f'{self.review[:15]}...'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Place, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('place')
        verbose_name_plural = _('places')
        ordering = ['-created_at']