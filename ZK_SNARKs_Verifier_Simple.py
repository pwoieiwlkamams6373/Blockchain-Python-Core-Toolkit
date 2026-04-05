class ZKSnarkVerifier:
    def verify(self, proof, public_input):
        return proof == hash(public_input)

if __name__ == "__main__":
    zk = ZKSnarkVerifier()
    print(zk.verify(hash(123),123))
