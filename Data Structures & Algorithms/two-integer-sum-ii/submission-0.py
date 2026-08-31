class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        l = len(numbers) - 1

        while f < l:
            sumTarget = numbers[f] + numbers[l]
            if sumTarget == target:
                return [f + 1, l + 1]
            if sumTarget > target:
                l -= 1
            else:
                f += 1
        
            