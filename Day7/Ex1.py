# Cho 2 set
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

# Tìm các bạn học cả toán lẫn vẽ
math_art = art_students.intersection(math_students)
print(math_art)

# Tìm những bạn học vẽ nhưng không học toán
study_art = (art_students - math_students)
print(study_art)

# Tìm những người bạn học toán nhưng không học vẽ
study_math = (math_students - art_students)
print(study_math)

# Tìm những người bạn chỉ học 1 môn
one_subject = (math_students ^ art_students)
print(one_subject)

# Tìm tất cả những người bạn
all_friends = (math_students | art_students)
print(all_friends)
