import uuid

class VoteSystem:
    def __init__(self):
        self.votes = {}

    def cast_vote(self, proposal_id, address, weight):
        if proposal_id not in self.votes:
            self.votes[proposal_id] = {}
        self.votes[proposal_id][address] = weight
        return True

    def resolve(self, proposals, proposal_id):
        if proposal_id not in self.votes:
            return None

        total_weight = sum(self.votes[proposal_id].values())
        approved = total_weight >= 100  # минимальный кворум

        for proposal in proposals:
            if proposal.id == proposal_id:
                return {
                    "id": proposal.id,
                    "title": proposal.title,
                    "description": proposal.description,
                    "approved": approved,
                    "action": proposal.action
                }

        return None
