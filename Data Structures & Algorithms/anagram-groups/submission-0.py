from collections import defaultdict
from typing import List

class Solution:
    # Approach:
    # 1. Sort each word to create a canonical key.
    # 2. Use a hash map to group words with the same key.
    # 3. Return all grouped anagram lists.
    #
    # Time Complexity: O(n * k log k)
    #   - n = number of strings
    #   - k = average length of each string
    #
    # Space Complexity: O(n * k)
    #   - stores all strings inside the groups
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)

        return list(groups.values())