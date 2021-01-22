from datetime import datetime

from ninja import Schema


class UserSchema(Schema):
    id: int
    username: str


class ArticleIn(Schema):
    author: int
    title: str
    content: str


class ArticleOut(Schema):
    id: int
    author: UserSchema
    created: datetime
    title: str
    content: str
