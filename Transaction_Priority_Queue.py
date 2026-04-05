import heapq

class TxPriorityQueue:
    def __init__(self):
        self.heap = []

    def add_tx(self, tx_id, gas_fee):
        heapq.heappush(self.heap, (-gas_fee, tx_id))

    def get_next_tx(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

if __name__ == "__main__":
    q = TxPriorityQueue()
    q.add_tx("tx1",50)
    q.add_tx("tx2",100)
    print("下一个交易:", q.get_next_tx())
