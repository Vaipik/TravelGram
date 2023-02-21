from uuid import uuid4

from django.db import models


class Event(models.Model):
    """"""
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4
    )
    title = models.CharField(

    )
    description = models.TextField(

    )
    slug =