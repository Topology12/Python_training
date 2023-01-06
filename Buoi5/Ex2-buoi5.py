students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
# Lấy thông tin sinh viên thứ nhất và in ra theo định dạng 
id = students[0][0]
name = students[0][1]
age = students[0][2]
print(f'''Id:{id}, name:{name} - age:{age}''')
#Lấy ra tuối sinh viên 2 
age_student_2 = students[0][2]
print(age_student_2)
#Lấy ra thông tin 2 sinh viên cuối
new_students = students[1:]
print(new_students)
# Lấy id cua sv thứ 3
id_student_3 = students[0][0]
print(id_student_3)