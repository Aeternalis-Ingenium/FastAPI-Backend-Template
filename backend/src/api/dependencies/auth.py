import fastapi
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.api.dependencies.repository import get_repository
from src.config.manager import settings
from src.repository.crud.account import AccountCRUDRepository
from src.securities.authorizations.jwt import jwt_generator
from src.utilities.exceptions.database import EntityDoesNotExist
from src.utilities.exceptions.http.exc_401 import http_exc_401_cunauthorized_request


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = fastapi.Depends(HTTPBearer()),
    account_repo: AccountCRUDRepository = fastapi.Depends(get_repository(repo_type=AccountCRUDRepository)),
):
    try:
        details = jwt_generator.retrieve_details_from_token(
            token=credentials.credentials,
            secret_key=settings.JWT_SECRET_KEY,
        )
    except (ValueError, Exception):
        raise await http_exc_401_cunauthorized_request()

    username = details[0]
    try:
        db_account = await account_repo.read_account_by_username(username=username)
    except EntityDoesNotExist:
        raise await http_exc_401_cunauthorized_request()
    return db_account
