class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []

        for indI, i  in enumerate(nums):
            for indJ, j in enumerate(nums):
                if indI != indJ:
                    if i+j == target:
                        indices.append(indI)
                        indices.append(indJ)
        
        final_indices = indices[0:2]
        return final_indices
        