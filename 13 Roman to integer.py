class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        #define dictionary with values
        romanNumerals = {
            "I" : 1,
            "V" : 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        #initialize total to count the number
        total = 0

        #loop through all of the characters in the roman numerals
        for i in range(len(s)):
            #set the current to the number inside the current numeral
            current = romanNumerals[s[i]]
            #if the next one is in bounds
            #and the current number is less then the next number
            #this is how roman numerals work
            if i+1 < len(s) and current < romanNumerals[s[i+1]]:
                #then you substract the current from total
                total -= current
            else:
                #otherwise just add the value
                total += current

        return total


        
