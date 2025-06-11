class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

       # Pointer to the last valid element in nums1 (the first m elements)
        index1 = m - 1

        # Pointer to the last element in nums2
        index2 = n - 1

        # Pointer to the last position in nums1 (m + n - 1)
        insert_index = m + n - 1

        # Iterate while there are elements to compare in both nums1 and nums2
        while index1 >= 0 and index2 >= 0:
            # Compare the current elements from nums1 and nums2
            # Place the larger one at the current insert position in nums1
            if nums1[index1] > nums2[index2]:
                nums1[insert_index] = nums1[index1]  # Move the larger element to the end of nums1
                index1 -= 1  # Move pointer in nums1 left
            else:
                nums1[insert_index] = nums2[index2]  # Move the larger (or equal) element from nums2
                index2 -= 1  # Move pointer in nums2 left
            insert_index -= 1  # Move the insert position to the left

        # If there are remaining elements in nums2 (nums1 is already in place if anything remains)
        while index2 >= 0:
            nums1[insert_index] = nums2[index2]  # Copy the leftover elements from nums2 into nums1
            index2 -= 1  # Move pointer in nums2 left
            insert_index -= 1  # Move the insert position to the left

        # No need to copy nums1's remaining elements — they are already in correct position
