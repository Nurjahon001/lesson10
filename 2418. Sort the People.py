class Solution:
    def sortPeople(self, names, heights):
        sorted_people = sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        sorted_names = [person[0] for person in sorted_people]
        return sorted_names

solution=Solution()
print(solution.sortPeople(["Mary","John","Emma"], [180,165,170]))