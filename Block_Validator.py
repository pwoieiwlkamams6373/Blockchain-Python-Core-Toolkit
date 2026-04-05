import hashlib
import json

class BlockValidator:
    def validate_block(self, block, previous_block):
        if block["previous_hash"] != self.hash_block(previous_block):
            return False
        if not self.valid_proof(previous_block["proof"], block["proof"]):
            return False
        return True

    def hash_block(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def valid_proof(self, last_proof, proof):
        guess = f"{last_proof}{proof}".encode()
        return hashlib.sha256(guess).hexdigest()[:4] == "0000"

if __name__ == "__main__":
    validator = BlockValidator()
    print("校验结果:", validator.valid_proof(100, 1234))
