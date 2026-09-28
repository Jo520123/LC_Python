from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :param deck: list[int]
        :return: list[int]
        """

        deck.sort()

        n = len(deck)
        res = [0] * n

        idx_queue = deque(range(n))

        for x in deck:
            res[idx_queue.popleft()] = x

            if idx_queue:
                idx_queue.append(idx_queue.popleft())

        return res
