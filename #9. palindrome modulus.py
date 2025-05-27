class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Edge cases:
        # 1. If x is negative, it's not a palindrome
        # 2. If x ends with 0 and is not 0 itself, it's not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverse = 0
        
        # Build the reverse number only up to half of x
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10
        
        # At the end, x should either be equal to reverse (even length)
        # Or x should be equal to reverse // 10 (odd length)
        return x == reverse or x == reverse // 10
