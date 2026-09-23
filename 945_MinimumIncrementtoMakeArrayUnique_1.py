class Solution:
    def minIncrementForUnique(self, nums):
        """
        :param nums: list[int]
        :return: int
        """
        nums.sort()
        move = 0
        minV = 0

        for x in nums:

            if x > minV:
                
                minV = x
               

            else:
             
                move += minV - x
                

            minV += 1
           

        return move

