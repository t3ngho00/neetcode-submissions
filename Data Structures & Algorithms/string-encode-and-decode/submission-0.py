class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "n" + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        l_nextword = ""
        while i < len(s):
            #finding out the length of the next word
            if s[i] != "n":
                l_nextword += s[i]
                i+=1
            else:
                length = int(l_nextword)
                l_nextword = ""
                next_i = i+1+length
                result.append(s[i+1:next_i])
                i = next_i
        return result

