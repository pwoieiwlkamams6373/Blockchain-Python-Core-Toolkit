import hashlib

class P2PSigner:
    def sign_message(self, msg, node_id):
        return hashlib.sha256(f"{msg}{node_id}".encode()).hexdigest()

if __name__ == "__main__":
    signer = P2PSigner()
    print(signer.sign_message("hello","node1"))
