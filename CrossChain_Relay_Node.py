class RelayNode:
    def relay_message(self, from_chain, to_chain, msg):
        return f"从{from_chain}中继到{to_chain}: {msg}"

if __name__ == "__main__":
    relay = RelayNode()
    print(relay.relay_message("ETH","BSC","测试消息"))
