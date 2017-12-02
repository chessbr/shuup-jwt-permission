# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from uuid import uuid4

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import gettext_lazy as _

from shuup.core.models import ShuupModel


@python_2_unicode_compatible
class APIApplication(ShuupModel):
    name = models.CharField(max_length=60, verbose_name=_("name"))
    key = models.CharField(max_length=64, verbose_name=_("app key"), editable=False, unique=True)
    enabled = models.BooleanField(default=True, verbose_name=_("enabled"))

    class Meta:
        verbose_name = _("api application")
        verbose_name_plural = _("api applications")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # create an unique key
        if not self.pk:
            self.key = "{}{}".format(uuid4().hex, uuid4().hex)
        return super(APIApplication, self).save(*args, **kwargs)


class APIApplicationPermission(models.Model):
    application = models.ForeignKey(APIApplication, related_name="permissions", verbose_name=_("api application"))
    permission = models.CharField(max_length=200, verbose_name=_("permission identifier"))
    granted = models.BooleanField(default=False, verbose_name=_("granted"))

    class Meta:
        unique_together = ("application", "permission")
        verbose_name = _("api application permission")
        verbose_name_plural = _("api application permissions")
