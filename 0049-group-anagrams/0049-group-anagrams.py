from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:
            dict[''.join(sorted(s))].append(s)
        return list(dict.values())