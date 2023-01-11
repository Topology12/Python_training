# Set nang cao 
# Cac phan tu cung o trong 2 set
set_1 = {1, 2, 5, 3}
set_2 = {1, 5, 8, 6}

set_3 = set_1.intersection(set_2)
print(set_3)
# Hoac su dung toan tu & 
print(set_1 & set_2)
# Phan bu cua set 
set_3 = set_1.difference(set_2)
print(set_3)
# Hoac 
print( set_1 - set_2)
# Hop cac set 
set_4 = set_1.union(set_2)
print(set_4)
print(set_1 | set_2 | set_3)
# Hop khong lay phan giao 
set_3 = set_1.symmetric_difference(set_2)
print(set_3)
# Dict
import json
student = {
    "name" :" Duong",
    "point" : 9.5, 
    "age" : 19,
}
print(json.dumps(student,indent=4))
# Loi khi tim key trong dict
# Lay key trong dict 
value = student.get("id" 'sv10')
print(value)
# Tao key moi cho dict
student["id"] = "SV1010"
print(student)
# Mo rong trong dict 
student.update(id="SV102", gender="Male")
print(json.dumps(student, indent=4))
