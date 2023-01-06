friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
print(friends)
# lấy 4 người bạn đầu trong list
head_friends = friends[0:4]
print(head_friends)
# lấy 4 người bạn cuối trong list
last_friends = friends[3:]
print(last_friends)
# đảo ngược list friends :
print(friends[::-1])
# Lấy các friend từ vị trí 1 đến hết
new_friends = friends[1:]
print(new_friends)
# Copy líst ban đầu thành list mới
friends_2 = friends[:]
print(friends_2)
# lấy ra những friends từ vt 2-> kế cuối
new_friends = friends[2:-1]
