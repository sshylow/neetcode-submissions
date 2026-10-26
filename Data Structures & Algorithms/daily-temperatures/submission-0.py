class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # indices of days still waiting for a warmer day

        for day, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                waiting_day = stack.pop()
                result[waiting_day] = day - waiting_day

            stack.append(day)

        return result