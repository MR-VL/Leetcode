class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #initialize variable to store max and result
        result = []
        maximum = 0

        #loop through all of the candies
        for i in range(len(candies)):
            #finds the maximum candy amount that one user has
            if candies[i]  >= maximum:
                maximum = candies[i]
        #loop through all of the candies
        for i in range(len(candies)):
            # if the current candy amount is greater save it
            if candies[i] + extraCandies >= maximum:
                result.append(True)
              #if less save it
            else:
                result.append(False)

        return result
