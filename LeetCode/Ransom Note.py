class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rannote,magz = Counter(ransomNote), Counter(magazine)
        if rannote & magz == rannote: return True
        return False
        
