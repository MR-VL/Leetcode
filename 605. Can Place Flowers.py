class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0
        # only one place in the flowerbed
        if len(flowerbed)==1:
            # if the flowerbed contains a zero
            if flowerbed[0] == 0:
                #add one to placed
                placed += 1
            #if placed greater or equal to amount needed return true otherwise false
            return placed >= n

        #loop through the flowerbed
        for i in range(len(flowerbed)):
            # first plot, verify is next plot itsnt placed, and current plot empty
            if i == 0 and flowerbed[i + 1] != 1 and flowerbed[i] == 0:
                #place flower 
                placed += 1
                flowerbed[i] = 1
            #last plot in the array, verify is previous plot itsnt placed, and current plot empty
            elif i == len(flowerbed) -1 and flowerbed[i - 1] != 1 and flowerbed[i] == 0:
                placed += 1
                flowerbed[i] = 1
            #middle plots, ensure within the array, and verify if next plot, and previous plots arent placed,
            #also ensure that current plot empty
            elif i< len(flowerbed) - 1 and flowerbed[i + 1] != 1 and flowerbed[i -1] != 1 and flowerbed[i] == 0:
                placed += 1
                flowerbed[i] = 1
            # if placed is equal to desired amount, auto return 
            if placed >= n:
                return True
        #the amount of flowers wanted to be placed is not possible return false
        return False
