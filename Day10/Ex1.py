# Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension

odd = even = 0
for i in range(0, 1001):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"So cac so le {odd}")
print(f"So cac so chan {even}")

lst = list(range(0, 1001))

lst_even = [n for n in lst if n % 2 == 0]
lst_odd = [n for n in lst if n % 2 != 0]
print(f"So cac so le {len(lst_odd)}")
print(f'So cac so chan {len(lst_even)}')
