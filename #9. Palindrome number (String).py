class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #create duplicate of x as string
        y= str(x)
        #reverse the duplicate
        y = y[::-1]
        #compare if string of x equals the reversed y
        if(str(x)==y):
            return True
        else:
            return False
        
