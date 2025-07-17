from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    subs = {}
    for index, number in enumerate(nums):
        if number in subs:
            return [subs[number], index] # return value and current index
        else:
            subs[target - number] = index
    return []

print(twoSum([2, 7, 11, 15], 9))

# Time complexity: O(n)
# Space complexity: O(n)

""" 
Practice writing it out

def twoSum(target: int, nums: List[int]) -> List[int]:
    sub = {}
    for index, number in enumerate(nums):
        if number in sub:
            return [sub[number], index]
        else:
            sub[target - number] = index
    return []

print(twoSum(9, [2, 7, 11, 15]))

# Time complexity: O(n)
# Space complexity: O(n)
"""