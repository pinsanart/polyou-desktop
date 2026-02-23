from pydantic import BaseModel, EmailStr
from uuid import UUID

class TokenRequest(BaseModel):
    email: EmailStr
    password: str

    device_id: UUID
    device_name: str