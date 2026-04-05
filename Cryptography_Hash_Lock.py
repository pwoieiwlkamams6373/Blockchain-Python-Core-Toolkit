import hashlib
import secrets

class HashLock:
    def create_secret(self):
        self.secret = secrets.token_hex(16)
        self.hash = hashlib.sha256(self.secret.encode()).hexdigest()
        return self.hash

    def unlock(self, secret):
        return hashlib.sha256(secret.encode()).hexdigest() == self.hash

if __name__ == "__main__":
    lock = HashLock()
    h = lock.create_secret()
    print("解锁结果:", lock.unlock(lock.secret))
