import hashlib
import time

class PoWMiner:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:self.difficulty] == "0" * self.difficulty

if __name__ == "__main__":
    miner = PoWMiner(difficulty=4)
    start = time.time()
    print("找到有效Nonce:", miner.proof_of_work(100))
    print("耗时:", time.time()-start, "秒")
