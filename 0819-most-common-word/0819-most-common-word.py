import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        filter_p = re.sub(r'\W', ' ', paragraph.lower())
        words = [word for word in filter_p.split() if word not in banned]
        counts = Counter(words)
        return counts.most_common(1)[0][0]