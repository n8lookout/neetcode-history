class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        result = float('inf')
        start, finish = -1, -1
        found = False

        for i in range(len(wordsDict)):
            word = wordsDict[i]
            if word == word1 or word == word2:
                if not found:
                    found = True
                    start = i
                elif found and finish > -1:
                    start = finish
                    finish = i
                    result = min(result, finish - start)
                else:
                    finish = i
                    result = min(result, finish - start)

        return result
