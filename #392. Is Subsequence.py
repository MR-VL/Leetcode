class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # Pointer to track position in s

        for char in t:  # Loop through each character in t
            # Check if we're still within bounds of s
            # If current character in t matches the character at position i in s,
            # it means we've found the next character in the subsequence
            if i < len(s) and s[i] == char:
                i += 1  # Move to the next character in s

        # If we've matched all characters in s, it's a valid subsequence
        return i == len(s)
