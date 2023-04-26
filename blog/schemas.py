from datetime import datetime
from django.contrib.auth.models import User
from ninja import ModelSchema, Schema


# Auto-schema generation for UserSchema
class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username'] 

# Manual schema generation for ArticleIn and ArticleOut
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