from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #finds the length of the gcd
        #for example in ABCABC as str1
        #and ABC as str2
        #the gcdLen -> the length of the GCD would be 3 as both strings have it
        gcdLen = gcd(len(str1), len(str2))

        #sets the candidate by extracting the length of the gcdLen from str1
        candidate = str1[:gcdLen]

        # (len(str1) // len(candidate)) divides the str by the length of the candidate
        #this is to find out the amount of times that the gcd candidate needs to repeat to form the original string

        # then candidate (the gcd string between the two) would be multiplied by the amount of times it needs to repeat
        #then it compares the second string to see if it can be made up of the same candidate
        if str1 == candidate * (len(str1) // len(candidate)) and str2 == candidate * (len(str2)//len(candidate)):
            #returns the candidate, which is the gcd
            return candidate
        #there is no gcd among the two strings
        else:
            return ""
