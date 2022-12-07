import datetime

import pydantic

from src.models.schemas.base import BaseSchemaModel


class AccountInCreate(BaseSchemaModel):
    username: str
    email: pydantic.EmailStr
    password: str


class AccountInUpdate(BaseSchemaModel):
    username: str | None
    email: str | None
    password: str | None


class AccountInLogin(BaseSchemaModel):
    username: str
    email: pydantic.EmailStr
    password: str


class AccountWithToken(BaseSchemaModel):
    token: str
    username: str
    email: pydantic.EmailStr
    is_verified: bool
    is_active: bool
    is_logged_in: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class AccountInResponse(BaseSchemaModel):
    id: int
    authorized_account: AccountWithToken
