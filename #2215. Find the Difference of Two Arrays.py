class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        #creates a set of each of the nums, if there are duplicates they are dropped
        set1 = set(nums1)
        set2 = set(nums2)

        #returns a list of the difference between set 1 and set 2 individually as a list
        #ex set1-set2 returns the values that are unique to set1 and that are not in set2
        #and the list is due to the way the problem is worded
        return  [list(set1 - set2), list(set2-set1)]
