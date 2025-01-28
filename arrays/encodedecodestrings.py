class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string

    def decode(self, s: str) -> list[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_strings.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return decoded_strings