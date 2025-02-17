'''
给你一个字符串 s ，请你反转字符串中 单词 的顺序。
'''
class solution:
    def reverseWord(self, str1):
        str2 = str1.strip()  # 去除前后空格
        list1 = str2.split()
        list1.reverse()
        str3 = ' '.join(list1)
        return str3

a = solution()
print(a.reverseWord('   i          love you '))
