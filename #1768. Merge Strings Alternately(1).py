class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #initialize final list
        final = []
        #find the max length of which word is bigger and then 
        #loop through all the characters of the max
        for i in range(max(len(word1), len(word2))):
            #if the current couter index is less then length of word
            #append the current character to the final list
            if i < len(word1):
                final.append(word1[i])
            if i < len(word2):
                final.append(word2[i])
        #required to join it to display nicely. join the final list into a string        
        return "".join(final)
