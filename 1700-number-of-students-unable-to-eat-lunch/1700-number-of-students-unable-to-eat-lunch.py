class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        A = deque(students)
        B = list(sandwiches) 
        count = 0
        while A and B:
            if A[0] == B[0]:
                A.popleft()
                B.pop(0)
                count = 0
            else:
                count += 1
                A.append(A.popleft())
            if count == len(A):
                return len(A)
        return 0
            