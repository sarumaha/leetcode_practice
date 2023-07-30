class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {
           "I":1,
           "V":5,
           "X":10,
           "L":50,
           "C":100,
           "D":500,
           "M":1000}
        
        special_symbols = {
           "IX":9,
           "IV":4,
           "XL":40,
           "XC":90,
           "CD":400,
           "CM":900
           }
        
        total = 0
        i = 0
        spec_symbol = False

        while i < len(s):
             if s[i:i+2] in special_symbols:
                the_symbol = s[i:i+2]
                total += special_symbols[the_symbol]
                i += 2
             elif s[i] in symbols:
                  total += symbols[s[i]]
                  i += 1
             else: 
                 print("error")
        
        return total