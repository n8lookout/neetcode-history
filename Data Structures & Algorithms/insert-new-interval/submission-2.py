class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # new interval start time is greater than intervals[i] end time
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            # new interval end time is less than intervals[i] start time
            elif newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            # overlapping - merge new interval with intervals[i]
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # new interval creates a merge of all existing intervals
        result.append(newInterval)
        
        return result