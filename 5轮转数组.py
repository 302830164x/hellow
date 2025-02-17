'''
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
'''
class solution:

    def rotate(self, nums, k):
        lenth1 = len(nums)
        list1 = [0] * lenth1

        # 记录列表的下标索引来交换数据，利用%可以实现轮转
        for i in range(lenth1):
            newindex = (i+k) % lenth1
            list1[newindex] = nums[i]

        for i in range(lenth1):
            nums[i] = list1[i]
        return nums

nums1 = [1,2,3,4,5,6,7,8]
a = solution()
print(a.rotate(nums1, 7))
