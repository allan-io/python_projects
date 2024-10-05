student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 300, 78, 65, 89, 86, 55, 91, 64, 89]

highest_num = student_scores[0]

for score in student_scores:
    if score > highest_num:
        highest_num = score

print(highest_num)

sum_var = 0
for num in range(1,101):
    sum_var += num

print(sum_var)