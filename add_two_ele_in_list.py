class Solution:
    #第一种方法，哈希表发
    def twoSum(self, nums, target):
        newdic={}
        result=[]
        for index,val in enumerate(nums):
            temp=target-val
            if temp in newdic:
                result.append(newdic[temp])
                result.append(index)
                return result
            else:
                if val in newdic:
                    continue
                else:
                    newdic[val]=index

    '''
            执行用时 :
        32 ms
        , 在所有 Python3 提交中击败了
        98.80%
        的用户
        内存消耗 :
        14.7 MB
        , 在所有 Python3 提交中击败了
        12.50%
        的用户
    '''
    #第二种方法，先排序,首尾递进查找
    def twoSum2(self,nums,target):
        dic = enumerate(nums)
        list_sorted = sorted(dic, key=lambda x: x[1])
        print(list_sorted)
        result = []
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = list_sorted[left][1] + list_sorted[right][1]
            if sum == target:
                result.append(list_sorted[left][0])
                result.append(list_sorted[right][0])
                return result
            elif sum < target:
                left = left + 1
            else:
                right = right - 1

    """
        执行用时 :
        44 ms
        , 在所有 Python3 提交中击败了
        89.74%
        的用户
        内存消耗 :
        15.4 MB
        , 在所有 Python3 提交中击败了
        5.07%
        的用户
    """


