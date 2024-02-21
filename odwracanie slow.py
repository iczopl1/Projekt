class Solution:
    def reverseWords(self, s: str) -> str:
        napis=[]
        word =''
        for letter in s:
            if letter != ' ':
                word +=letter
            if letter == ' ' and word!='':
                napis.append(word)
                word =''
            if letter == ' ' and word =='':
                word = ''
        napis.append(word)
        napis =napis[::-1]
        if napis[0]=='':
            napis.pop(0)
        odp = ' '.join(napis)
        return odp

x = Solution()
s=' a  good  example '
print(x.reverseWords(s))