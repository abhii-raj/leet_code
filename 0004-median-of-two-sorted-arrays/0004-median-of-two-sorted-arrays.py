class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        c=0
        for i in range (len(nums3)):
            if nums3[i] == 0:
                c += 1
        if c == len(nums3):
            return(0)
        if len(nums3) == 1:
            return(nums3[0])
        a = -1
        for i in range (len(nums3)):
            if nums3[i-1] != nums3[i]:
                a += 1
        if (len(nums3)-1)%2 == 0:
                    med = (len(nums3)-1)//2
                    return(nums3[med])
        else:
                    meds = (len(nums3)-1)//2
                    med = (nums3[meds]+nums3[meds+1])
                    return(med/2)

        