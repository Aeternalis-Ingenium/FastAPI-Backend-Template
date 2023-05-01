import datetime

import pydantic


class JWToken(pydantic.BaseModel):
    exp: datetime.datetime
    sub: str


class JWTAccount(pydantic.BaseModel):
    username: str
    email: pydantic.EmailStr
