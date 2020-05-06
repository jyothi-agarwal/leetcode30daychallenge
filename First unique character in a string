from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
       dict = Counter(s)
       for i in s:
            if dict[i] == 1:
                return s.index(i)
       return -1
