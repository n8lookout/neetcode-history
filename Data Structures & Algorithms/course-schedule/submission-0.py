class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = { c:[] for c in range(numCourses)}

        # populate ajacency list
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            if prereq[course] == []:
                return True

            cycle.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            prereq[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True