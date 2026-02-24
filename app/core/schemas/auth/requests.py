from pydantic import BaseModel, EmailStr
from uuid import UUID

class TokenRequest(BaseModel):
    username: EmailStr
    password: str

    device_id: UUID
    device_name: str

class RefreshRequest(BaseModel):
    refresh_token: str

class LogoutRequest(BaseModel):
    refresh_token: str
