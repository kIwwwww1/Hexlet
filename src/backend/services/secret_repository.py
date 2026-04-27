import bcrypt


class SecretRepository:
    @classmethod
    def hash_password(cls, user_password: str) -> str:
        pwd_bytes = user_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(pwd_bytes, salt)

        return hashed.decode('utf-8')

    @classmethod
    def verify_password(cls, input_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(
            input_password.encode('utf-8'), hashed_password.encode('utf-8')
        )
