# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #boundries given in problem
        low = 1
        high = n
        # keeps the loop running 
        while low<= high:
            #finds the middle between the two values
            middle = (low + high) // 2
            #guesses at the middle
            result = guess(middle)
            #result is found and it is the middle
            if result == 0: 
                return middle

            # guess was higher so take values less then middle and set it to high bound
            if result == -1:
                high = middle - 1 
             # guess was lower so take values higher then middle and set it to low bound
            else:
                low = middle + 1 



    
