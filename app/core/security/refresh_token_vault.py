import keyring

class RefreshTokenVault:
    def __init__(self, service_name: str):
        self.service_name = service_name

    def _key(self, username:str):
        return f"{username}_refresh_token"
    
    def save(self, username:str, refresh_token:str) -> str:
        keyring.set_password(self.service_name, self._key(username), refresh_token)

    def get(self, username:str) -> str:
        return keyring.get_password(self.service_name, self._key(username))

    def delete(self, username: str):
        keyring.delete_password(self.service_name, self._key(username))