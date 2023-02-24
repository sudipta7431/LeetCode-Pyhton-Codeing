class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 = nums1 + nums2
        a = sorted(list1)
        n = len(a)
        if n % 2 == 0:
            return (a[int((n/2))-1]+a[int(n/2)])/2
        else:
            return a[int(n/2)]