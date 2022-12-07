import typing

import sqlalchemy
from sqlalchemy.orm import DeclarativeBase


class DBTable(DeclarativeBase):
    metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()


Base: typing.Type[DeclarativeBase] = DBTable
