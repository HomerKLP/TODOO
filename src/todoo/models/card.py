from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.entity import Entity


class Card(Entity):
    uuid = models.UUIDField(
        primary_key=True, verbose_name=_('uuid'), default=uuid4,
    )
    name = models.CharField(
        max_length=64, verbose_name=_('name'),
    )
    user = models.ForeignKey(
        to='common.ExtendedUser', verbose_name=_('user'),
        on_delete=models.DO_NOTHING,
    )
    category = models.ForeignKey(
        to='todoo.Category', verbose_name=_('category'),
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        verbose_name = _('Card')
        verbose_name_plural = _('Cards')
