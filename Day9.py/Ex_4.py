# Đếm số lượng số nguyên tố trong [1, 100]
sum_n = 0
for n in range(2, 101):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        sum_n += 1
print(sum_n)
