class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        h1 = {}
        for i in nums1:
            if i in h.keys():
                h[i]=h[i]+1
            else:
                h[i]=1
        for i in nums2:
            if i in h1.keys():
                h1[i]=h1[i]+1
            else:
                h1[i]=1
        ans = []
        for i in h:
            if i in h1:
                count = min(h[i],h1[i])
                for _ in range(count):
                    ans.append(i)
        return ans            

        