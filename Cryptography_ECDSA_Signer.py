import ecdsa
import hashlib

class ECDSASigner:
    def __init__(self):
        self.sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.vk = self.sk.get_verifying_key()

    def sign_message(self, message):
        msg_hash = hashlib.sha256(message.encode()).digest()
        signature = self.sk.sign(msg_hash)
        return signature.hex()

    def verify_message(self, message, signature_hex):
        msg_hash = hashlib.sha256(message.encode()).digest()
        signature = bytes.fromhex(signature_hex)
        try:
            return self.vk.verify(msg_hash, signature)
        except:
            return False

if __name__ == "__main__":
    signer = ECDSASigner()
    sig = signer.sign_message("区块链签名测试")
    print("签名验证结果:", signer.verify_message("区块链签名测试", sig))
