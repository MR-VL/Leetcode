class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #initialize count to store total number of zeros
        totalZero = 0
        #store the length of nums in the array
        length = len(nums)
        #loop through all the values inside the array
        for num in range(length):
            # count the number of total zeros to be used later
            if num == 0:
                totalZero += 1

        #keeps track of how many elements have been inserted so far
        insertPos = 0
        #loop through the array again
        for num in range(length):
            #if current index is an actual number 
            if nums[num] != 0:
                #insert it into the array, this does not insert zeros and therefore counter is used to keep track of positions
                nums[insertPos] = nums[num]
                #increment to move on to the next index
                insertPos += 1
        # the total amount of real numbers inserted and the difference between total length
        while insertPos < length:
            # just inserts the rest of the zeros starting off from where it finished with the real nums
            nums[insertPos] = 0
            insertPos +=1 