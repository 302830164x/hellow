class Solution():

    def merge(self, nums1, m, nums2, n):
        for iw in range(n):
            nums1[m+iw] = nums2[iw]
        for ie in range(len(nums1)):
            for j in range(len(nums1)-ie-1):
                if nums1[j]>nums1[j+1]:
                    h = nums1[j]
                    nums1[j] = nums1[j+1]
                    nums1[j+1] = h
        return nums1

a = Solution()
b = a.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
for i in range(len(b)):
    print(b[i], end=' ')

