class SimpleGradebook:
    def __init__(self):
        self._grades = {}
    def add_student(self, name):
        self._grades[name] = []
    def report_grade(self, name, score):
        self._grades[name].append(score)
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)
S = SimpleGradebook()
S.add_student("Nicolay Bliski")
S.report_grade('Nicolay Bliski', 90)
S.report_grade('Nicolay Bliski', 95)
S.report_grade('Nicolay Bliski', 85)
print(S.average_grade("Nicolay Bliski"))
