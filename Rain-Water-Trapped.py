class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        capacityFromLeft = [0] * len(A)
        capacityFromRight = [0] * len(A)
        localHigh = A[0]

        for i in range(1, len(A)):
            diff = localHigh - A[i]
            localHigh = max(localHigh, A[i])

            if ( diff > 0):
                capacityFromLeft[i] = diff
            else:
                capacityFromLeft[i] = 0
        
        localHigh = A[-1]
        for i in range(len(A)-2, -1, -1):
            diff = localHigh - A[i]
            localHigh = max(localHigh, A[i])

            if ( diff > 0):
                capacityFromRight[i] = diff
            else:
                capacityFromRight[i] = 0
        
        totalCapacity = 0
        for i in range(len(A)):
            totalCapacity += min(capacityFromLeft[i], capacityFromRight[i])

        return totalCapacity