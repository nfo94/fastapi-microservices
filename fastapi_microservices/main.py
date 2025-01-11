from enum import Enum
from fastapi import FastAPI
from typing import Optional, Dict
from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


app = FastAPI()


valid_users = dict()
valid_profiles = dict()
pending_users = dict()
discussion_posts = dict()
request_headers = dict()
cookies = dict()


class User(BaseModel):
    username: str
    password: str


class ValidUser(BaseModel):
    id: UUID
    username: str
    password: str
    passphrase: Optional[str]


class UserType(str, Enum):
    admin = "admin"
    teacher = "teacher"
    alumni = "alumni"
    student = "student"


class UserProfile(BaseModel):
    first_name: str
    last_name: str
    middle_initial: str
    age: Optional[int] = None
    salary: Optional[float] = None
    birthday: date
    user_type: UserType


class PostType(str, Enum):
    information = "information"
    inquiry = "inquiry"
    quote = "quote"
    twit = "twit"


class Post(BaseModel):
    topic: Optional[str] = None
    message: str
    date_posted: datetime


class ForumPost(BaseModel):
    id: UUID
    topic: Optional[str] = None
    message: str
    post_type: PostType
    date_posted: datetime
    username: str


def check_password():
    pass


@app.get("/")
async def home():
    return {"message": "Home"}


@app.get("/login")
async def login(username: str, password: str):
    if valid_users.get(username) is None:
        return {"message": "User does not exist"}

    user = valid_users.get(username)
    if check_password(password.encode(), user.passphrase.encode()):
        return user
    else:
        return {"message": "Invalid user"}


@app.get("/login/signup")
async def signup(username: str, password: str):
    if username is None or password is None:
        return {"message": "Invalid user"}
    if valid_users.get(username) is not None:
        return {"message": "User already exists"}

    user = User(username=username, password=password)
    pending_users[username] = user
    return user


@app.put("/account/profile/update/{username}")
async def update_profile(username: str, id: UUID, new_profile: UserProfile):
    if valid_users.get(username) is None:
        return {"message": "User does not exist"}

    user = valid_users.get(username)
    if user.id == id:
        valid_profiles[username] = new_profile
        return {"message": "Successfully updated"}


@app.patch("/account/profile/update/names/{username}")
async def update_profile_names(username: str, id: UUID, new_names: Dict[str, str]):
    if valid_users.get(username) is None:
        return {"message": "User does not exist"}
    if new_names is None:
        return {"message": "New names are required"}

    user = valid_users.get(username)
    if user.id != id:
        return {"message": "User does not exist"}

    profile = valid_profiles[username]
    profile.first_name = new_names["fname"]
    profile.last_name = new_names["lname"]
    profile.middle_initial = new_names["mi"]
    valid_profiles[username] = profile
    return {"message": "Profile successfully updated"}


@app.delete("/discussion/posts/remove/{username}")
async def delete_discussion(username: str, id: UUID):
    if valid_users.get(username) is None:
        return {"message": "User does not exist"}
    if discussion_posts.get(id) is None:
        return {"message": "Post does not exist"}

    del discussion_posts[id]
    return {"message": "Post deleted"}
