import time

class Timelock:
    def __init__(self, delay=3600):
        self.delay = delay
        self.queue = {}

    def queue_tx(self, tx_id):
        self.queue[tx_id] = time.time()

    def execute_tx(self, tx_id):
        if tx_id in self.queue and time.time()-self.queue[tx_id]>=self.delay:
            return True
        return False

if __name__ == "__main__":
    tl = Timelock(1)
    tl.queue_tx(1)
    time.sleep(1)
    print("执行:", tl.execute_tx(1))
