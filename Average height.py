student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_of_heights = sum(student_heights)
average = sum_of_heights / len(student_heights)
print(f"The average height is: {round(average)}")
