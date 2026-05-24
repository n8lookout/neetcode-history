class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        letter_to_index = {}

        for i in range(len(keyboard)):
            letter_to_index[keyboard[i]] = i

        prev = 0
        result = 0

        for c in word:
            result += abs(prev - letter_to_index[c])
            prev = letter_to_index[c]

        return result