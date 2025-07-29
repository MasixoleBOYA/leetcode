class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) >= 1 and len(s) <= 15:
            valid_numerals = {
                "I" :1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
            }
            counter = 0
            i = 0

            while i < len(s):
                # Check for subtractive combination
                if i + 1 < len(s) and valid_numerals[s[i]] < valid_numerals[s[i + 1]]:
                    counter += valid_numerals[s[i + 1]] - valid_numerals[s[i]]
                    i += 2  # Skip the next character because it's part of the pair
                else:
                    counter += valid_numerals[s[i]]
                    i += 1

            return counter

        else:
            raise ValueError("Roman is not between 1 and 15")
        