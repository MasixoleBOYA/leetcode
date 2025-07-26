class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ''
        
        i = 0
        while i < len(word1) and i < len(word2):
            word3 += word1[i] + word2[i]
            i += 1

        if len(word1)>len(word2):
            word3+= word1[i:]
        else:
            word3 += word2[i:]


        return word3
        
        