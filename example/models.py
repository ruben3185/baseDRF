

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from baseDRF.models import AuditModel


class Example(AuditModel):
    description = models.TextField('Description', null=True, blank=True, default=None)
    name = models.TextField('Name', null=True, blank=True, default=None)

    def __int__ (self):
        return self.id