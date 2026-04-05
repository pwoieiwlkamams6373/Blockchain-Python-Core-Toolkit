from cryptography.fernet import Fernet

class AESEncryptor:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode()).hex()

    def decrypt(self, encrypted_hex):
        data = bytes.fromhex(encrypted_hex)
        return self.cipher.decrypt(data).decode()

if __name__ == "__main__":
    aes = AESEncryptor()
    enc = aes.encrypt("区块链加密数据")
    print("解密结果:", aes.decrypt(enc))
