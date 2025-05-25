class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        #initialize list to store the final merged string
        final = []

        #find the maximum length, of either word 1 or word 2
        #then using the maximum length loop through all the characters
        #the maximum may be greater then the other word
        for i in range(max(len(word1), len(word2))):
            #ensure tat i representing the current index
            #is less then the length meaning that there are still
            #characters in the word
            
            # if one word runs out it will simply skip and will still append
            #the characters from the other word
            if i < len(word1):
                #if there are still characters append them to final
                final.append(word1[i])

            #works the same as the previous    
            if i < len(word2):    
                final.append(word2[i])

        # return back and use "".join() function to turn it back from a list 
        #to a string 
        return "".join(final)
