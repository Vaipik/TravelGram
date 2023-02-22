from uuid import uuid4

from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models

from .libs import constants


User = get_user_model()


class Event(models.Model):
    """Event model"""
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4
    )
    title = models.CharField(
        max_length=constants.TITLE_MAX_LENGTH,
        verbose_name="Event title"
    )
    description = models.TextField(
        verbose_name="Description of event"
    )
    slug = AutoSlugField(
        populate_from="title",
        unique_with=("title", "owner"),
        verbose_name="Event url",
        max_length=constants.TITLE_MAX_URL
    )
    started_at = models.DateField(
        null=False,
        blank=False,
        verbose_name="Start of event"
    )
    ended_at = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="End of event"
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="owner"
    )

    class Meta:
        db_table = "user_event"
        ordering = ("title", "duration")
        unique_together = ("title", "owner")
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self) -> str:
        return f"[{self.owner}] {self.title}"

    @property
    def duration(self) -> int:
        if self.ended_at is None:
            return 0  # Event has no duration

        return (self.ended_at - self.started_at).days  # For example if event it is a vacation
