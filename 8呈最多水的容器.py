'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
'''

class solution:
    def maxArea(self, list1):
        '''
        采用左右指针的方法，移动较矮的线，当两个指针重合即停止
        '''
        left, right = 0, len(list1)-1
        areas = []
        while left < right:
            area = (right - left) * min(list1[left], list1[right])
            # area = min(list1[left], list1[right]) * (right - left)
            areas.append(area)
            if list1[left] < list1[right]:
                left+=1
            elif list1[left] > list1[right]:
                right-=1
            elif list1[left] == list1[right]:
                left+=1
        areas.sort(reverse=True)
        return areas[0]

list2 = [1,8,6,2,5,4,8,3,7]
a = solution()
print(a.maxArea(list2))