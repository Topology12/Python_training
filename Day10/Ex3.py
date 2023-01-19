# Cho dict như sau:
import json
people = {
    "Emma": 71,
    "Jack": 45,
    "Amy": 15,
    "Ben": 29
}

# In ra nguoi lon tuoi nhat
max_age = 0
name = ""
for n, a in people.items():
    if a >= max_age:
        max_age = a
        name = n
print(name)

# Tạo ra một dict mới dựa vào people dict với tuổi của mỗi người tăng gấp đôi
new_people = {
    name: age*2
    for name, age in people.items()
}
print(new_people)

# In ra enumerate các key trong people dict
print(list(enumerate(people)))

# Sử dụng hàm dict để biến enumerate bên trên trở thành dict
new_people_1 = dict(list(enumerate(people)))
print(json.dumps(new_people_1, indent=4))
