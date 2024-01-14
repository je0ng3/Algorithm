import sys

total = 0
creditSum = 0
grade_ = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
gradeNum = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
for _ in range(20):
  name, credits, grade = list(sys.stdin.readline().split())
  credits = float(credits)
  if grade in grade_:
    total += (credits * gradeNum[grade_.index(grade)])
    creditSum += credits
print(round(total/creditSum,5))