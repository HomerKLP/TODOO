from cryptography.fernet import Fernet
from django.conf import settings


class Encryptor:
    fernet = Fernet(settings.SECRET_KEY)

    def __init__(self, text: str) -> None:
        self.text = text

    def encrypt(self) -> str:
        return self.fernet.encrypt(self.text.encode()).decode()

    def decrypt(self) -> str:
        return self.fernet.decrypt(self.text.encode()).decode()
