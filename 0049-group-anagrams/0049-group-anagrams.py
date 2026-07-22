class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=collections.defaultdict(list)
        for s in strs:
            s_ = ''.join(sorted(s))
            hashmap[s_].append(s)
        return list(hashmap.values())