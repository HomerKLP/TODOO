def test_encryption():
    text = 'my_secret_text'
    enc = Encryptor(text=text)
    encryptex_text = enc.encrypt()
    assert text != encryptex_text
    assert text == Encryptor(text=encryptex_text).decrypt()
