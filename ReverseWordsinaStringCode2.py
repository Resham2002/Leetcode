class Solution(object):
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])
             
            
   
        

sol = Solution()
print(sol.reverseWords("  hello world  "))