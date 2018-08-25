#encoding:utf-8

__author__ = 'zhoupao'
__date__ = '2018/8/24 22:48'

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        # 循环遍历出来
        for index, value in enumerate(nums):
            sub = target - value
            if sub in dic:
                return [dic[sub], index]
            else:
                dic[value] = index

if __name__ == '__main__':
    s=Solution()
    # nums = [2, 7, 11, 15], target = 9
    lis1=s.twoSum([2, 7, 11, 15],9)
    print(lis1)
