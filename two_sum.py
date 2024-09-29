class Solution:
    def two_sum(self, nums: list[int], target: int) -> int:
        # one pass hash map
        # hash map structure -> key: num[index], value: index
        hash_map = {}
        for i in range(0, len(nums)):
            if nums[i] in hash_map:
                # putting the hash map value before because ideally
                # any entry in the hash map would be an earlier index 
                return [hash_map[nums[i]], i]
            else:
                # if element not already in hash map then store difference from target as key
                # to facilitate search using hash map
                hash_map[target - nums[i]] = i
        return []

sol = Solution()
print(sol.two_sum([2,7,11,15],9))
print(sol.two_sum([3,2,4],6))
print(sol.two_sum([3,3],6))
