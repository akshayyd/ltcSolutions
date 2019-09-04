class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        last_character = 'M'
        char_counter_I = 0
        char_counter_X = 0
        char_counter_C = 0
        char_counter_M = 0
        
        for char in s:
            result += roman_dict[char]
            if roman_dict[last_character] < roman_dict[char]:
                result -= roman_dict[last_character]*2
            last_character = char
            if last_character == char:
                if char == 'I':
                    char_counter_I +=1
                if char == 'X':
                    char_counter_X +=1
                if char == 'C': 
                    char_counter_C +=1
                if char == 'M':
                    char_counter_M +=1
            if char_counter_I > 3 or char_counter_X > 4 or char_counter_C>4 or char_counter_M >4:
                    return -1
            
        return result
        