from uuid import uuid4

from django.db import models

from ..libs import constants


class FileCategory(models.Model):
    """Model for user image/video"""
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4
    )
    name = models.CharField(
        max_length=constants.DESCRIPTION_MAX_LENGTH,
        verbose_name="File category"
    )