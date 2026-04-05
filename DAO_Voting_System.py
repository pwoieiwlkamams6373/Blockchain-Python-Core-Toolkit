class DAOVoting:
    def __init__(self):
        self.proposals = {}

    def create_proposal(self, pid, content):
        self.proposals[pid] = {"content":content, "yes":0, "no":0}

    def vote(self, pid, choice):
        if pid in self.proposals and choice in ["yes","no"]:
            self.proposals[pid][choice] +=1

    def get_result(self, pid):
        return self.proposals.get(pid, None)

if __name__ == "__main__":
    dao = DAOVoting()
    dao.create_proposal(1,"升级提案")
    dao.vote(1,"yes")
    print(dao.get_result(1))
