from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from common.models.entity import Entity, EntityUserManager


class ExtendedUser(Entity, AbstractUser):
    objects = EntityUserManager()

    def save(self, *args, **kwargs):
        self.email = self.username
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
