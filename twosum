class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #declare list of previously encountered numbers
        prev = {}
       
        #declare an index that it is currently looping through
        # declare a num var that will be used to enumerate (loop through) all of the nums
        for index, num in enumerate(nums):
            #holds the complement of the target - current number 
            #this will be used to look through to see if the current number + a previous number 
            #will make the sum
            targ = target - num


            # if targ which is target - current number is in previous
            if  targ in prev:
                # if the complement is in prev
                #return prev of the complement, and the index of the current 
                return [prev[targ], index]
            
            #if the current number complement + any number in previous dont make the target
            #add this index to search further
            prev[num] = index
            
            
