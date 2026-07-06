class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        h = {}
        ans = []
        for i in a:
            original = i

            sorted_val = ' '.join(sorted(i))
            if sorted_val in h:
                h[sorted_val].append(original)
            else:
                h[sorted_val]=[original]
        for key,values in h.items():
            ans.append(values)
        return ans                

        