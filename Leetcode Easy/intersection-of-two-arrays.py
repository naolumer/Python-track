class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1= Counter(nums1)
        count2 = Counter(nums2)
        answer = []
        for key,freq in count1.items():
            if key in count2:
                answer.append(key)
        return answer