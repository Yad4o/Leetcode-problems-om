class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        B = deque(deck)
        A = deque()
        result = [0] * len(deck)
        for i in range(len(deck)):
            A.append(i)
        while A:
            ind = A.popleft()
            result[ind] = B.popleft()
            if A:
                A.append(A.popleft())
        return result