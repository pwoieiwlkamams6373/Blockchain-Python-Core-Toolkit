import secrets

class MnemonicGenerator:
    words = ["apple","banana","cherry","date","elderberry","fig","grape","honey","ice","juice"]
    def generate(self, length=12):
        return " ".join([secrets.choice(self.words) for _ in range(length)])

if __name__ == "__main__":
    mg = MnemonicGenerator()
    print("助记词:", mg.generate())
