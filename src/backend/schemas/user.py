from random import sample
from string import ascii_lowercase, ascii_uppercase, digits
from pydantic import BaseModel, Field, EmailStr

_LOWERCASE = ascii_lowercase
_UPPERCASE = ascii_uppercase
_DIGITS = digits

def generate_unique_id(
        use_lower: int = 2,
        use_upper: int = 2,
        use_digits: int = 2,
    ) -> str:
    '''Creating a unique user ID and used default value (2)'''

    random_lower = sample(_LOWERCASE, use_lower)
    random_upper = sample(_UPPERCASE, use_upper)
    random_digit = sample(_DIGITS, use_digits)
    combined = random_lower + random_upper + random_digit
    
    return ''.join(sample(combined, len(combined)))

class UserData(BaseModel):
    user_name: str = Field(min_length=3, max_length=15)
    email: EmailStr
    password: str = Field(min_length=8, max_length=25)


class UserNewData(UserData):
    unique_id: str = Field(default_factory=generate_unique_id)
    

