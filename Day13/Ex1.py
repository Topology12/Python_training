# Tạo một class hình chữ nhật chứa hai thuộc tính: chiều dài và chiều rộng
# Tạo các method để tính chu vi và diện tích của hình chữ nhật
# Tạo đối tượng hình chữ nhật và gọi các method tương ứng
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def circum(self):
        return (self.width+self.length)*2

    def area(self):
        return self.width*self.length


rec_one = Rectangle(2, 3)

circum_one = rec_one.circum()
print(f'Chu vi cua hinh chu nhat la : {circum_one}')

area_one = rec_one.area()
print(f'Dien tich hinh chu nhat la: {area_one}')
