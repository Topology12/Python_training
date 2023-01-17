# Nhập vào một số nguyên dương n tính tổng các chữ số của n.
n = int(input("Nhap so nguyen n= "))

while n <= 0:
    print("Nhap n phai la so nguyen duong ")
    n = int(input("Nhap vao n= "))

sum_n = 0
while n > 0:
    dv = n % 10
    sum_n += dv
    n //= 10

print(f"So cac so nguyen to", sum_n)
