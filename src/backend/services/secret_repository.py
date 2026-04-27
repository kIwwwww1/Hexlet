from passlib.context import CryptContext


class SecretRepository:
    _pwd_context = CryptContext(schemes=['bcrypt'])

    @classmethod
    def hash_password(cls, user_password: str) -> str:
        return cls._pwd_context.hash(user_password)

    @classmethod
    def verify_password(cls, input_password: str, hashed_password: str) -> bool:
        return cls._pwd_context.verify(input_password, hashed_password)
