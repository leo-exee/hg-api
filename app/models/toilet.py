from enum import Enum

from pydantic import BaseModel

from app.models.mongo import MongoModel, PyObjectId


class lockSystemEnum(str, Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    NO_LOCK = "no_lock"


class DaysOfWeekEnum(str, Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


class Review(BaseModel):
    rating: int
    state: int
    cleanliness: int
    accessbility: int
    comment: str


class Location(BaseModel):
    lat: float
    long: float


class OpeningInfo(BaseModel):
    day: DaysOfWeekEnum
    allDay: bool
    allHours: bool
    openHour: int
    closeHour: int


class Information(BaseModel):
    rating: int
    state: int
    cleanliness: int
    accessbility: int
    babyFriendly: bool
    handicapFriendly: bool
    lockSystem: lockSystemEnum
    openingHours: list[OpeningInfo]
    maintenancePhoneNum: str


class ToiletInDAO(MongoModel):
    name: str
    address: str
    location: Location
    information: Information
    reviews: list[Review]


class ToiletOutDTO(ToiletInDAO):
    id: PyObjectId
