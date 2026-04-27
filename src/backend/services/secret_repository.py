from passlib.context import CryptContext


class SecretRepository:
    __pwd_context = CryptContext(schemes=['bcrypt'])

    def hash_password(self, user_password: str) -> str:
        return self.__pwd_context.hash(user_password)

    def verify_password(self, input_password: str, hashed_password: str) -> bool:
        return self.__pwd_context.verify(input_password, hashed_password)
