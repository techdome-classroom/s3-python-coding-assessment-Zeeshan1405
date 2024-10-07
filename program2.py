class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to map Roman numerals to their corresponding values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse the string in reverse
        for char in reversed(s):
            curr_value = roman_map[char]
            
            # If current value is less than the previous value, subtract it
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            
            # Update previous value to the current one
            prev_value = curr_value
        
        return total
