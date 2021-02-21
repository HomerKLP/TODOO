from todoo.helpers import Encryptor


def test_encryption():
    text = 'my_secret_text'
    enc = Encryptor(text=text)
    encrypted_text = enc.encrypt()
    assert text != encrypted_text
    assert text == Encryptor(text=encrypted_text).decrypt()
