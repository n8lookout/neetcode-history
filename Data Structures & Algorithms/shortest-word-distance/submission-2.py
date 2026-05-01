class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ptr1, ptr2 = -1, -1
        minDist = len(wordsDict)

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                ptr1 = i
            elif wordsDict[i] == word2:
                ptr2 = i

            if ptr1 != -1 and ptr2 != -1:
                minDist = min(minDist, abs(ptr1 - ptr2))

        return minDist