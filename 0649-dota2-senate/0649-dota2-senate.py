class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        R = deque()
        D = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)
        while R and D:
            a = R.popleft()
            b = D.popleft()
            if a < b:
                R.append(a + len(senate))
            else:
                D.append(b + len(senate))
        if R:
            senate = "Radiant"
            return senate
        else:
            senate = "Dire"
            return senate