class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #creates a current sum from beginning to how many values requested
        currentSum = sum(nums[:k])
        #records the maximum as the current
        maximum = currentSum
        #loops through the array from the current value k since we calculated the previous, all the way to the end
        for i in range(k, len(nums)):
            #remove the previous element from the array (the first one added) and add the next element to calculate sum
            currentSum = currentSum - nums[i-k] + nums[i]
            # sets the maximum to eiter the previous or current depending on which is bigger
            maximum = max(maximum, currentSum)

        #returns the average
        return maximum / k
