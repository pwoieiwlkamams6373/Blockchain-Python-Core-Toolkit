import random

class ZKPSimple:
    def __init__(self, secret):
        self.secret = secret
        self.p = 104729

    def generate_proof(self):
        r = random.randint(1, self.p-1)
        x = pow(r, 2, self.p)
        c = random.randint(0,1)
        if c == 0:
            y = r
        else:
            y = (r * self.secret) % self.p
        return x, c, y

    def verify_proof(self, x, c, y):
        if c == 0:
            return pow(y,2,self.p) == x
        else:
            return pow(y,2,self.p) == (x * pow(self.secret,2,self.p)) % self.p

if __name__ == "__main__":
    zkp = ZKPSimple(1234)
    proof = zkp.generate_proof()
    print("零知识证明验证:", zkp.verify_proof(*proof))
