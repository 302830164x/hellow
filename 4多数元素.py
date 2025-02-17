
b = [1,1,1,2,3,2,3,2,2,2,2]

class solution:

    def majortyelement(self,nums):
        n = len(nums) / 2
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1
            if counts[num] > n:
                return num

a = solution()
print(a.majortyelement(b))