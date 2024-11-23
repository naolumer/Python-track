class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicc= {}
        
        counter= len(nums)
        for num in nums:
            if num in dicc:
                dicc[num]+=1
            else:
                dicc[num]=1
                    
        for keys in dicc:
            if dicc[keys]!=2:
                n= keys
        return n