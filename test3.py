class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
    # 取较小值
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            merged += word1[i] + word2[i]
    
    # 如果word1更长，将剩余的部分添加到merged的末尾
        if len(word1) > min_len:
            merged += word1[min_len:]
    # 否则，将word2的剩余部分添加到merged的末尾
        else:
            merged += word2[min_len:]
    
        return merged