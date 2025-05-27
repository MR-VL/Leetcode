# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import random
class Solution:
    def guessNumber(self, n: int) -> int:
        #declarations given in problem
        found = False
        minimum = 1
        maximum = 2**31 - 1
        #creates a random number between given in statement
        number = random.randint(minimum, maximum)

        #loop until solution is found
        while not found:
            #this is the return from the api
            choose = guess(number)

            #if found return
            if choose == 0: 
                return number
            elif choose == -1: 
                #number less then guess set max to current 
                maximum = number
            else:
                #number greater then guess set min to current
                minimum = number
            # regen number
            number = random.randint(minimum, maximum)
