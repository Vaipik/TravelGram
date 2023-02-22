from enum import Enum
from pathlib import Path
from typing import Optional

from django.utils import timezone
from django.db.models import FileField


class Categories(Enum):
    """Allowed file categories and their extensions"""
    IMAGES = ("jpeg", "png", "jpg", "svg")
    VIDEOS = ("mp4", "mov", "mkv")


def determine_category(extension: str) -> Optional[str]:
    """returns category name by file extension"""

    for category in Categories:
        if extension in category.value:
            return category.name


def _get_folder_name(instance, filename: str) -> str:
    """
    This function is used with FileField to define folder name by file extension.
    :param instance: FileField instance
    :param filename: file which extension should be defined
    :return: string with following format 'category/y/m/d/uuid.ext'
    """
    if type(instance) != FileField:
        raise ValueError(f"{_get_folder_name.__name__} function must be used only with FileField")

    extension = Path(filename).suffix[1:]
    folder_name = determine_category(extension)
    current_date = timezone.now().date()
    new_filename = instance.pk + extension  # Changing filename to instance UUID
    new_file_path = f"{folder_name}/{current_date}/{new_filename}"

    return new_file_path
