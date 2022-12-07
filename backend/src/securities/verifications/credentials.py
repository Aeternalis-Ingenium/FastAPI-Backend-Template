class CredentialVerifier:
    def is_username_available(self, username: str | None) -> bool:
        if username:
            return False
        return True

    def is_email_available(self, email: str | None) -> bool:
        if email:
            return False
        return True


def get_credential_verifier() -> CredentialVerifier:
    return CredentialVerifier()


credential_verifier: CredentialVerifier = get_credential_verifier()
