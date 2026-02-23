import keyring

class AuthTokensVault:
    def __init__(self, service_name: str):
        self.service_name = service_name

    def _access_token_key(self, username: str):
        return f"{username}_access_token"

    def _refresh_token_key(self, username:str):
        return f"{username}_refresh_token"

    def save_access_token(self, username: str, access_token: str) -> None:
        keyring.set_password(self.service_name, self._access_token_key(username), access_token)
    
    def save_refresh_token(self, username:str, refresh_token:str) -> str:
        keyring.set_password(self.service_name, self._refresh_token_key(username), refresh_token)

    def get_access_token(self, username: str) -> str:
        return keyring.get_password(self.service_name, self._access_token_key(username))
    
    def get_refresh_token(self, username:str):
        keyring.get_password(self.service_name, self._refresh_token_key(username))

    def delete_access_token(self, username: str):
        keyring.delete_password(self.service_name, self._access_token_key(username))

    def delete_refresh_token(self, username: str):
        keyring.delete_password(self.service_name, self._refresh_token_key(username))

    def delete_all(self, username: str):
        self.delete_access_token(username)
        self.delete_refresh_token(username)