'''
Approach (sorting): Count frequencies with a hashmap, 
sort by frequency descending, slice first k.

Time Complextiy: O(n log n)
Space Complexty: O(n)
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [x for x, _ in count.most_common(k)] 