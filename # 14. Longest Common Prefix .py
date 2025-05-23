class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #assumes that the prefix is in the first string and takes
        #the entire first string and assigns it as prefix
        prefix = strs[0]

        #since we assigned prefix to strs[0] we start from 1 with this one
        for string in strs[1:]:
            #if the string does not start with the prefix
            while not string.startswith(prefix):
                #remove one character from the end of the prefix
                #this loop will continue to run until either it finds the common prefix among all of them or end up 
                #removing everything from the prefix
                prefix = prefix[:-1]

                #if there is no common prefix found return empty
                if not prefix:
                    return ""
        #return prefix            
        return prefix
