class DAGBlockchain:
    def __init__(self):
        self.units = {}
        self.genesis = "genesis"
        self.units[self.genesis] = []

    def add_unit(self, unit_id, parents):
        for p in parents:
            if p not in self.units:
                return False
        self.units[unit_id] = parents
        return True

if __name__ == "__main__":
    dag = DAGBlockchain()
    print(dag.add_unit("unit1",["genesis"]))
