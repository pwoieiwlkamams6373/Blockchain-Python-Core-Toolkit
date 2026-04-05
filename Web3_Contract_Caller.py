class Web3Caller:
    def call_contract(self, addr, func, params=[]):
        return f"调用{addr}的{func}函数，参数{params}"

if __name__ == "__main__":
    caller = Web3Caller()
    print(caller.call_contract("0x123","transfer",["0x456",100]))
