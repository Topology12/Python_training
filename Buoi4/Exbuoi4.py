movies_watched = ["One piece", "Avatar",
                  "Kimetsu no Yaiba", "Dragon balls", "The conjuring"]
print(movies_watched)
# Nhap phim moi va dua vao cuoi list
new_movie = input("Nhap vao ten mot bo phim: ")
movies_watched.append(new_movie)
print(movies_watched)
# In ra phim Dau - Giua - Cuoi cua list
print(movies_watched[0])
print(movies_watched[2])
print(movies_watched[3])
print(movies_watched[5])
# Tong so phim co trong list
print(len(movies_watched))
# Xoa phim dau va cuoi list
movies_watched.remove(movies_watched[0])
movies_watched.remove(movies_watched[-1])
# Lay movie cuoi va xoa no khoi list
last_movie = movies_watched.pop()
print(last_movie)
# Chen 1 movie vao dau list
movies_watched.insert(0, "gió")
print(movies_watched)
# Dem so movie co ten la "One piece"
print(movies_watched.count("One piece"))
# Tim vi tri phim co ten la "gio"
movies_watched.index("gió")
# Them 1 danh sach cac bo phim vao cuoi list
movies_watched.extend(["Kungfu panda", "Vua hài kịch", "Đại thoại tây du"])
# Xoa tat ca phim co trong list
movies_watched.clear()
