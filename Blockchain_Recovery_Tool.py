class RecoveryTool:
    def recover_wallet(self, mnemonic):
        return f"根据助记词恢复: {mnemonic[:10]}..."

if __name__ == "__main__":
    rt = RecoveryTool()
    print(rt.recover_wallet("apple banana cherry date elderberry fig grape"))
