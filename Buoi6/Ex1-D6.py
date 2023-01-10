friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
print(friends)

# Lấy chiều dài của tuple friends
print(len(friends))

# Lấy các phần tử đầu, cuối, giữa và kiểu của chúng
head = friends[0]
last = friends[-1]
between = friends[1]
print(type(head))
print(type(last))
print(type(between))

# Nhập vào tên và giới tinh sau đó append vào list friends
name = input("Nhập vào name: ")
gender = input("Nhập vào giới tính: ")
tup = (name, gender)
friends.append(tup)
print(friends)
