class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    # 创建字典来统计s和t中每个字符的出现次数
        s_count = {}
        t_count = {}
    
    # 统计字符串s中每个字符的出现次数
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
    
    # 统计字符串t中每个字符的出现次数
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
    
    # 遍历t的字符计数字典，找出在t中比s中多出现1次的字符
        for char in t_count:
            if t_count[char] - s_count.get(char, 0) == 1:
                return char