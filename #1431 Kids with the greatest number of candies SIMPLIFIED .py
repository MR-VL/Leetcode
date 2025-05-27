class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #saves the maximum amount of candies in the array 
        maximum = max(candies)
        result = []
        #loop through all of the candies
        for i in range(len(candies)):
            #if current + extra greater or equal put true otherwise false
            if candies[i] + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result
