from enum import Enum
from pathlib import Path
from typing import Optional


class Categories(Enum):
    """Allowed file categories and their extensions"""
    IMAGES = ("jpeg", "png", "jpg", "svg")
    VIDEOS = ("mp4", "mov", "mkv")


def determine_category(file: str) -> Optional[str]:
    """returns category name by file extension"""
    extension = Path(file).suffix[1:]

    for category in Categories:
        if extension in category.value:
            return category.name
