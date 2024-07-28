# Solution for - https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        res = 0
        i = 0

        while i < len(s)-1:
            calc = 0
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                print("In first if condition")
                calc = abs(dic['I'] - dic[s[i+1]])
                res += calc
                print("index = "+str(i)+" calc value = "+str(calc)+ " res = "+str(res))
                i += 1
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                print("In second if condition")
                calc = abs(dic['X'] - dic[s[i+1]])
                res += calc
                print("index = "+str(i)+" calc value = "+str(calc)+ " res = "+str(res))
                i += 1
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                print("In third if condition")
                calc = abs(dic['C'] - dic[s[i+1]])
                res += calc
                print("index = "+str(i)+" calc value = "+str(calc)+ " res = "+str(res))
                i += 1
            else:
                print("In final else condition")
                res += dic[s[i]]
                print("index = "+str(i)+" calc value = "+str(calc)+ " res = "+str(res))
            i += 1
            
        if i == len(s)-1:
            res += dic[s[i]]
        # else:
        #     res += dic[s[i+1]]
            
        return res



'''
Better solution

def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        current_value = roman_values[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    
    return total


'''
