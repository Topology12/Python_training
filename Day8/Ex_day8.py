# Nhập vào số nguyên n và kiểm tra tính chẵn lẻ 
n = int(input("Nhap vào số nguyên n= "))
if n % 2 == 0:
    print("Số chẵn")
else: 
    print("Số lẻ")

# Nhập vào 1 năm và kiểm tra nó có phải năm nhuận 
year= int(input("Nhập vào 1 năm: "))

if year % 400 == 0 or ((year % 4 == 0) and (year % 100 == 0)):
    print("Năm nhuận")
else:
    print("Năm không nhuận")

# Nhập 2 số nguyên a và b..Tìm số lớn nhất trong a và b
a = int(input("Nhập số nguyên a= "))
b = int(input("Nhập số nguyên b= "))
max = a
if b>max: 
    max = b
print(max)

# Giải và biện luận no cua pt bậc nhất 1 ân 
a = int(input("Nhâp vào hệ số a= "))
b = int(input("Nhập vào b= "))
if a==0:
    if b==0: 
        print("Phương trình có vô số no")
    else: 
        print("Phương trình vô nghiệm") 
else: 
    print("Phương trình có no duy nhât x=", -b/a)

# giải và biện luận no pt bậc hai 
a = int(input("Nhâp vào hệ số a= "))
b = int(input("Nhập vào b= "))
c = int(input("Nhập vào c= "))
delta = (b**2) - 4*a*c
if delta>0:  
    x1=(-b + delta**1/2)/(2*a) 
    x2=(-b - delta**1/2)/(2*a) 
    print(f"Phương trình có 2 no phân biệt x1={x1}, x2={ x2}")
elif delta==0:
    print("Phương trình có no kép x1 = x2 =",-b/(2*a))
else: 
    print("Phương trình vô nghiệm")