grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()

dict_students = {}
dict_students[students_list[0]] = float(sum(grades[0]) / len(grades[0]))
dict_students[students_list[1]] = float(sum(grades[1]) / len(grades[1]))
dict_students[students_list[2]] = float(sum(grades[2]) / len(grades[2]))
dict_students[students_list[3]] = float(sum(grades[3]) / len(grades[3]))
dict_students[students_list[4]] = float(sum(grades[4]) / len(grades[4]))
print(dict_students)
