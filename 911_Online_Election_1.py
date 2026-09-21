from collections import defaultdict
import bisect

class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :param persons: list[int]
        :param times: list[int]
        """

        self.times = times
        self.leader = []
        maxVote = 0
        vote_dic = defaultdict(int)

        current_candidate = 0

        for p in persons:
            vote_dic[p] += 1

            if vote_dic[p] >= maxVote:
                maxVote = vote_dic[p]
                current_candidate = p

            self.leader.append(current_candidate)

    def q(self, t):
        idx = bisect.bisect_right(self.times,t) - 1

        return self.leader[idx]
