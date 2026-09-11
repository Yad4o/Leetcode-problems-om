class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        B = deque(deck)
        A = deque(range(len(deck)))
        result = [0] * len(deck)
        while A:
            ind = A.popleft()
            result[ind] = B.popleft()
            if A:
                A.append(A.popleft())
        return result