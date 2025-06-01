class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Start from the third-to-last step and move backward to the first step
        for i in range(len(cost) - 3, -1, -1):
            # Update cost[i] to be the cost of this step plus the cheaper option of the next one or the one after that
            cost[i] += min(cost[i + 1], cost[i + 2])
            # This means: minimal total cost starting at step i = cost at i + min cost from next steps

        # After updating all steps, the minimal cost to start from step 0 or step 1 is the answer
        return min(cost[0], cost[1])
