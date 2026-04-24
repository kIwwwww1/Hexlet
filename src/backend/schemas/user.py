from pydantic import BaseModel, Field, EmailStr

class UserData(BaseModel):
    user_name: str = Field(min_length=3, max_length=15)
    user_email: EmailStr
    user_password: str = Field(min_length=8, max_length=25)

