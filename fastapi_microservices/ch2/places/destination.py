from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel


class TourType(str, Enum):
    resort = "resort"
    hotel = "hotel"
    bungalow = "bungalow"
    tent = "tent"
    exclusive = "exclusive"


class AmenitiesTypes(str, Enum):
    restaurant = "restaurante"
    pool = "poll"
    beach = "beach"
    shops = "shops"
    bars = "bars"
    activities = "activities"


class TourBasicInfo(BaseModel):
    id: UUID
    name: str
    type: TourType
    amenities: List[AmenitiesTypes]
