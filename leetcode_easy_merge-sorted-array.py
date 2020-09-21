# Instruction:
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        self.num1 = nums1
        self.num2 = nums2
        
        # replace 0 in nums1 by nums2 element
        for i in range(len(self.num1)):
            if self.num1[i] == 0:
                self.num1[i] = self.num2.pop()
                
        # sorting
        i = 0
        while i < len(self.num1) - 1:
            if self.num1[i] > self.num1[i+1]:
                self.num1[i], self.num1[i+1] = self.num1[i+1], self.num1[i]
                i = -1
            i += 1
                
        return self.num1
