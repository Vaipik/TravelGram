from uuid import uuid4

from django.db import models

from utils.file_categories import _get_folder_name
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
    file = models.FileField(
        upload_to=_get_folder_name
    )

    category = models.ForeignKey(
        to="file.FileCategory",
        on_delete=models.CASCADE,
        related_name="category",
    )
    event = models.ForeignKey(
        to="event.Event",
        on_delete=models.CASCADE,
        related_name="event"
    )

    class Meta:
        db_table = "event_files"
        verbose_name = "File"
        verbose_name_plural = "Files"
        ordering = [""]
