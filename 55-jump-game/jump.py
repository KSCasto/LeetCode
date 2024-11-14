from typing import List
class Solution:
    def tryJump(self, distance, hop, nums: List[int], visited: List[int]) -> bool:
        madeIt = False
        tryHop = hop

        if distance in visited:
            return False
        visited.add(distance)

        while madeIt == False and tryHop > 0:
            #if we can hit the goal
            if distance + tryHop >= len(nums)-1:
                madeIt = True
            #if there's room to go and the next hop isn't 0
            elif nums[distance + tryHop] > 0:
                madeIt = self.tryJump(distance + tryHop, nums[distance + tryHop], nums, visited)
            tryHop -= 1
            
        return madeIt

    def canJump(self, nums: List[int]) -> bool:
        madeIt = False
        visited = set()
        
        if len(nums) <= 1:
            madeIt = True
        elif self.tryJump(0, nums[0], nums, visited) == True:
            madeIt = True
        
        return madeIt
    
def test_runner():
    winnable = Solution()
    test_cases = [([2,5,0,0], True),
    ([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6], True),
    ([3,2,1,0,4], False),
    ([0], True),
    ([2,0], True),
    ([1,0,1,0], False)]

    for nums, expected in test_cases:
       result = winnable.canJump(nums)
       print(f"Input: {nums}")
       print(f"Expected: {expected}, Got: {result}")
       print(f"{'PASS' if result == expected else 'FAIL'}\n")

test_runner()
