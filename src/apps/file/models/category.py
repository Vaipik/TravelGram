from django.db import models

from ..libs import constants


class FileCategory(models.Model):
    """Model for user image/video"""
    name = models.CharField(
        max_length=constants.DESCRIPTION_MAX_LENGTH,
        primary_key=True,
        editable=False,
        verbose_name="File category"
    )
