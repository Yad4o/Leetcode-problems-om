class Solution:
    def buildArray(self, target, n):
        ans = []
        j = 0

        for i in range(1, n + 1):
            if j == len(target):
                break

            ans.append("Push")

            if i == target[j]:
                j += 1
            else:
                ans.append("Pop")

        return ans