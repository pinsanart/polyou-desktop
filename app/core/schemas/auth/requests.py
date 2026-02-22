from pydantic import BaseModel, EmailStr

class TokenRequest(BaseModel):
    email: EmailStr
    password: str