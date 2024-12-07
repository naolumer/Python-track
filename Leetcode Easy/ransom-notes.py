
def canConstruct(ransomNote, magazine):
      
        magazine_counts = {}
    
        for char in magazine:
            if char in magazine_counts:
                magazine_counts[char] += 1
            else:
                magazine_counts[char] = 1
        
        for char in ransomNote:
            if char in magazine_counts and magazine_counts[char] > 0:
                magazine_counts[char] -= 1
            else:
                return False
        
        return True