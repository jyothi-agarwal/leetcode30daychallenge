from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: 
        return all(ransomNote.count(r) <= magazine.count(r) for r in set(ransomNote))
