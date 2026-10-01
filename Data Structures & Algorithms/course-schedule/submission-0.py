class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {c:[] for c in range(numCourses)}
        count = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            count[course] +=1

        ready = [c for c in range(numCourses) if count[c] == 0]
        taken = 0

        while ready: 
            c = ready.pop()
            taken +=1
            for child in graph[c]:
                count[child] -= 1
                if count[child] == 0:
                    ready.append(child)

        return taken == numCourses
