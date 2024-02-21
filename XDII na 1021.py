class Solution:
    def romanToInt(self, s: str) -> int:
        i = 1
        s=s+'J'
        wynik = 0
        odjecie = 0
        for litera in s:
            if litera == "J":
                i=i-1
            if litera == 'M':
                wynik =wynik+1000
            if litera == 'C' and s[i]=='M':
                wynik =wynik-100
            elif litera == 'C' and s[i]=='D':
                wynik =wynik-100
            elif litera == 'C':
                wynik =wynik+100
            if litera == 'D':
                wynik =wynik+500
            if litera == "X" and s[i]=="L":
                wynik =wynik-10
            elif litera == "X" and s[i]=="C":
                wynik =wynik-10
            elif litera == "X":
                wynik =wynik+ 10
            if litera == "I" and s[i]=="X":
                wynik =wynik-1
            elif litera == "I" and  s[i]=="V":
                wynik =wynik-1
            elif litera == "I":
                wynik =wynik+ 1
            if litera == "L":
                wynik =wynik+ 50
            if litera == "V":
                wynik =wynik+ 5
            i =i+1
        return wynik
Roz = Solution()
s= 'MCMXCIV'
print(Roz.romanToInt(s))

