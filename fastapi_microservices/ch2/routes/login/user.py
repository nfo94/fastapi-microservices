from fastapi import APIRouter
from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel

from ..places.destination import TourBasicInfo

pending_users = dict()
approved_users = dict()

router = APIRouter()


class Signup(BaseModel):
    username: str
    password: str
    firstname: str
    lastname: str
    birthday: datetime


class User(BaseModel):
    id: UUID
    username: str
    password: str


class Tourist(BaseModel):
    id: UUID
    login: User
    date_signed: datetime
    booked: int
    tours: List[TourBasicInfo]


@router.post("/user/signup")
async def signup(signup: Signup):
    pass
