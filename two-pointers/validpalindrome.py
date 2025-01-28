class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ''
        
        for char in s:
            if char.isalnum():
                filtered_string += char.lower()
        return filtered_string == filtered_string[::-1]