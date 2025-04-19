from proposal import Proposal
from vote import VoteSystem

class DAO:
    def __init__(self):
        self.proposals = []
        self.voting = VoteSystem()

    def submit_proposal(self, title, description, action):
        proposal = Proposal(title, description, action)
        self.proposals.append(proposal)
        return proposal.id

    def vote(self, proposal_id, voter_address, weight):
        return self.voting.cast_vote(proposal_id, voter_address, weight)

    def execute(self, proposal_id):
        proposal = self.voting.resolve(self.proposals, proposal_id)
        if proposal and proposal["approved"]:
            print("EXECUTED:", proposal["action"])
            return True
        return False
