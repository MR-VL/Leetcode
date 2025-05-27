class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Calculate the total sum of the array
        total = sum(nums)
        leftSum = 0

        # Iterate through the array
        for i in range(len(nums)):
            # At index i, the left sum is the sum of elements before i
            # The right sum can be calculated by subtracting leftSum and nums[i] from total
            # If left sum equals right sum, we've found the pivot index
            if leftSum == total - leftSum - nums[i]:
                return i

            # Add the current element to leftSum for the next iteration
            leftSum += nums[i]

        # If no pivot index is found, return -1
        return -1
