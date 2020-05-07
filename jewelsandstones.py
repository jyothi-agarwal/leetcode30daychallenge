from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dict = Counter(S)
        count = 0
        for i in J:
            count=count + dict[i]
        return count
