grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
new_students = list(students)
new_students.sort()
count0 = sum(grades[0])
count1 = sum(grades[1])
count2 = sum(grades[2])
count3 = sum(grades[3])
count4 = sum(grades[4])
avg0 = count0/len(grades[0])
avg1 = count1/len(grades[1])
avg2 = count2/len(grades[2])
avg3 = count3/len(grades[3])
avg4 = count4/len(grades[4])
new_grades = [[avg0],[avg1],[avg2],[avg3],[avg4]]
all_avg = dict(zip(new_students,new_grades))
print(all_avg)