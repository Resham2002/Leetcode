class Solution(object):
    def compress(self, chars):
        i = 0 
        write = 0 
        while i < len(chars):
            curr = chars[i]
            count = 0
            

            while i < len(chars) and chars[i] == curr:
                i += 1
                count += 1

            chars[write] = curr
            write += 1
            
     
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        

        return write
