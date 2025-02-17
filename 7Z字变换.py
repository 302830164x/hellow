'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
'''

class solution:
    def Z_change(self, str1, n):
        list1 = [''] * n  # 用来保存n行的列表
        current_idex = 0  # 每行最新的索引
        m = 1             # 为1时向下遍历，为-1时向上遍历
        if n >= len(str1):
            return str1
        '''
        思考：遍历从索引0开始，向下遍历，到n-1时，则向上遍历，
        通过判断这两个节点来定义+-1来实现向上向下
        关键就是控制索引，来遍历字符串分别保存到每一行中
        '''
        for i in str1:
            list1[current_idex] = list1[current_idex] + i
            if current_idex == 0:
                m = 1
            elif current_idex == n-1:
                m = -1
            current_idex += m
        str1 = ''.join(list1)
        return str1
a = solution()
print(a.Z_change('PAYPALISHIRING', 3))
