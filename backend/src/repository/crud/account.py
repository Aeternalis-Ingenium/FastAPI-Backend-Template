import typing

import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.account import Account
from src.models.schemas.account import AccountInCreate, AccountInLogin, AccountInUpdate
from src.repository.crud.base import BaseCRUDRepository
from src.securities.hashing.password import pwd_generator
from src.securities.verifications.credentials import credential_verifier
from src.utilities.exceptions.database import EntityAlreadyExists, EntityDoesNotExist
from src.utilities.exceptions.password import PasswordDoesNotMatch


class AccountCRUDRepository(BaseCRUDRepository):
    async def create_account(self, account_create: AccountInCreate) -> Account:
        new_account = Account(username=account_create.username, email=account_create.email, is_logged_in=True)

        new_account.set_hash_salt(hash_salt=pwd_generator.generate_salt)
        new_account.set_hashed_password(
            hashed_password=pwd_generator.generate_hashed_password(
                hash_salt=new_account.hash_salt, new_password=account_create.password
            )
        )

        self.async_session.add(instance=new_account)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_account)

        return new_account

    async def read_accounts(self) -> typing.Sequence[Account]:
        stmt = sqlalchemy.select(Account)
        query = await self.async_session.execute(statement=stmt)
        return query.scalars().all()

    async def read_account_by_id(self, id: int) -> Account:
        stmt = sqlalchemy.select(Account).where(Account.id == id)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist("Account with id `{id}` does not exist!")

        return query.scalar()  # type: ignore

    async def read_account_by_username(self, username: str) -> Account:
        stmt = sqlalchemy.select(Account).where(Account.username == username)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist("Account with username `{username}` does not exist!")

        return query.scalar()  # type: ignore

    async def read_account_by_email(self, email: str) -> Account:
        stmt = sqlalchemy.select(Account).where(Account.email == email)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist("Account with email `{email}` does not exist!")

        return query.scalar()  # type: ignore

    async def read_user_by_password_authentication(self, account_login: AccountInLogin) -> Account:
        stmt = sqlalchemy.select(Account).where(
            Account.username == account_login.username, Account.email == account_login.email
        )
        query = await self.async_session.execute(statement=stmt)
        db_account = query.scalar()

        if not db_account:
            raise EntityDoesNotExist("Wrong username or wrong email!")

        if not pwd_generator.is_password_authenticated(hash_salt=db_account.hash_salt, password=account_login.password, hashed_password=db_account.hashed_password):  # type: ignore
            raise PasswordDoesNotMatch("Password does not match!")

        return db_account  # type: ignore

    async def update_account_by_id(self, id: int, account_update: AccountInUpdate) -> Account:
        new_account_data = account_update.dict()

        select_stmt = sqlalchemy.select(Account).where(Account.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        update_account = query.scalar()

        if not update_account:
            raise EntityDoesNotExist(f"Account with id `{id}` does not exist!")  # type: ignore

        update_stmt = sqlalchemy.update(table=Account).where(Account.id == update_account.id).values(updated_at=sqlalchemy_functions.now())  # type: ignore

        if new_account_data["username"]:
            update_stmt = update_stmt.values(username=new_account_data["username"])

        if new_account_data["email"]:
            update_stmt = update_stmt.values(username=new_account_data["email"])

        if new_account_data["password"]:
            update_account.set_hash_salt(hash_salt=pwd_generator.generate_salt)  # type: ignore
            update_account.set_hashed_password(hashed_password=pwd_generator.generate_hashed_password(hash_salt=update_account.hash_salt, new_password=new_account_data["password"]))  # type: ignore

        await self.async_session.execute(statement=update_stmt)
        await self.async_session.commit()
        await self.async_session.refresh(instance=update_account)

        return update_account  # type: ignore

    async def delete_account_by_id(self, id: int) -> str:
        select_stmt = sqlalchemy.select(Account).where(Account.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        delete_account = query.scalar()

        if not delete_account:
            raise EntityDoesNotExist(f"Account with id `{id}` does not exist!")  # type: ignore

        stmt = sqlalchemy.delete(table=Account).where(Account.id == delete_account.id)

        await self.async_session.execute(statement=stmt)
        await self.async_session.commit()

        return f"Account with id '{id}' is successfully deleted!"

    async def is_username_taken(self, username: str) -> bool:
        username_stmt = sqlalchemy.select(Account.username).select_from(Account).where(Account.username == username)
        username_query = await self.async_session.execute(username_stmt)
        db_username = username_query.scalar()

        if not credential_verifier.is_username_available(username=db_username):
            raise EntityAlreadyExists(f"The username `{username}` is already taken!")  # type: ignore

        return True

    async def is_email_taken(self, email: str) -> bool:
        email_stmt = sqlalchemy.select(Account.email).select_from(Account).where(Account.email == email)
        email_query = await self.async_session.execute(email_stmt)
        db_email = email_query.scalar()

        if not credential_verifier.is_email_available(email=db_email):
            raise EntityAlreadyExists(f"The email `{email}` is already registered!")  # type: ignore

        return True
