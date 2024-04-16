class Solution(object):
    def reverseWords(self, s):
        temp = ""
        res = ""
        s = s.strip()
        s = " ".join(s.split())
        for i in reversed(range(len(s))):
            temp += s[i]
            if s[i] == " ":
                temp = temp[::-1]
                res += temp
                temp = ""
        
        return (res +" "+ temp[::-1]).strip()
             
            
   
        

sol = Solution()
print(sol.reverseWords("  hello world  "))