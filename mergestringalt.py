class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        res = ""       #Empty string to append the char's
        i,j = 0,0      # 0,0 looks like a face

        while i < len(word1) and j < len(word2):

            res = res + word1[i]
            i += 1
            res = res + word2[j]
            j += 1
        
        # while i < len(word1):
        #     res = res + word1[i]
        #     i += 1

        # while j < len(word2):
        #     res = res + word2[j]
        #     j += 1

        return res + word1[i:] + word2[j:]
    
sol = Solution()
print(sol.mergeAlternately("ab","pqrs"))