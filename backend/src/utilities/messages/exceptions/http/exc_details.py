def http_400_username_details(username: str) -> str:
    return f"The username {username} is taken! Be creative and choose another one!"


def http_400_email_details(email: str) -> str:
    return f"The email {email} is already registered! Be creative and choose another one!"


def http_400_signup_credentials_details() -> str:
    return "Signup failed! Recheck all your credentials!"


def http_400_sigin_credentials_details() -> str:
    return "Signin failed! Recheck all your credentials!"


def http_401_unauthorized_details() -> str:
    return "Refused to complete request due to lack of valid authentication!"


def http_403_forbidden_details() -> str:
    return "Refused access to the requested resource!"


def http_404_id_details(id: int) -> str:
    return f"Either the account with id `{id}` doesn't exist, has been deleted, or you are not authorized!"


def http_404_username_details(username: str) -> str:
    return f"Either the account with username `{username}` doesn't exist, has been deleted, or you are not authorized!"


def http_404_email_details(email: str) -> str:
    return f"Either the account with email `{email}` doesn't exist, has been deleted, or you are not authorized!"
