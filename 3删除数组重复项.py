class Solution:

## 使用快慢指针，慢指针slow用来存放不重复的元素，快指针用来遍历
    def removeDupliactes(self, nums):
        slow = 0
        len1 = len(nums)
        for fast in range(1, len1):
            if nums[fast] != nums[slow]:
                slow = slow + 1
                nums[slow] = nums[fast]
        return slow+1


