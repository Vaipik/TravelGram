from uuid import uuid4

from django.db import models

from ..libs import constants


class File(models.Model):
    """Model for user image/video"""
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4
    )
    description = models.CharField(
        max_length=constants.DESCRIPTION_MAX_LENGTH,
        null=True,
        blank=True,
        verbose_name="File description"
    )
    event = models.ForeignKey(
        to="event.Event",
        on_delete=models.CASCADE,
        related_name="event"
    )

