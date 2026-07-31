class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        nums1.extend(nums2)
        for id,val in nums1: 
            d[id]+= val
        return sorted([[id, d[id]] for id in d])