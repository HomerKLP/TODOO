from django.contrib.auth.models import UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class EntityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(  # pragma: no cover
            is_deleted=False
        )


class EntityUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_deleted=False
        )


class Entity(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created_at'),
    )
    modified_at = models.DateTimeField(
        auto_now=True, verbose_name=_('modified_at'),
    )
    is_deleted = models.BooleanField(
        default=False, verbose_name=_('is_deleted'), db_index=True,
        editable=False,
    )

    objects = EntityManager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save(*args, **kwargs)

    class Meta:
        abstract = True
