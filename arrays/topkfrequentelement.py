class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        
        return [item[0] for item in sorted_items[:k]]
