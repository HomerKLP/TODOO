from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.entity import Entity
from todoo.helpers import Encryptor


class Card(Entity):
    uuid = models.UUIDField(
        primary_key=True, verbose_name=_('uuid'), default=uuid4,
    )
    _name = models.TextField(
        verbose_name=_('name'),
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

    @property
    def name(self) -> str:
        return Encryptor(text=self._name).decrypt()

    @name.setter
    def name(self, value) -> None:
        self._name = Encryptor(text=value).encrypt()
