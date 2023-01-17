# Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n]
old = 0 
even = 0 
n = int(input("Nhap vao n= "))

while n<= 0:
    print("n phai la so nguyen duong")
    n = int(input("Nhap vao n= "))
for i in range(1,n+1):
    if i % 2 != 0:
        old += 1 
    else:
        even +=1 
print(f"So so le trong doan = {old}")
print(f"So so chan trong doan = {even}")
