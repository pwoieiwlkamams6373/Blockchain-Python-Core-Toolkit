class FullNodeSync:
    def sync_chain(self, local_chain, remote_chain):
        if len(remote_chain) > len(local_chain):
            return remote_chain
        return local_chain

if __name__ == "__main__":
    sync = FullNodeSync()
    local = [1,2,3]
    remote = [1,2,3,4]
    print("同步后:", sync.sync_chain(local, remote))
