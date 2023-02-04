# Tạo menu có các chức năng của một app quản lý sách
# Thêm một cuốn sách
# Hiển thị tất cả các cuốn sách
# Xóa các cuốn sách theo id
# Tìm kiếm các cuốn sách theo id
# Lưu ý: dữ liệu về các cuốn sách lưu trữ trong file json
import json
USER_MENU = '''
Các chức năng:
    'a' : Thêm một cuốn sách
    'd' : Hiển thị tất cả các cuốn sách 
    'r' : Xóa các cuốn sách theo id 
    'f' : Tìm kiếm sách theo id
    'q' : Thoát 

    Nhập lựa chọn của bạn: 
'''
book_file = "info_book.json"
prevs = set()
try:
    with open("info_book.json", 'x') as book_file:
        json.dump([], book_file)
except FileExistsError:
    pass


def add_book():
    book_id = input("Nhap id cuon sach: ")
    while book_id in prevs:
        print("Id không hợp lệ, vui lòng nhập lại id.")
        book_id = input("Nhap id cuon sach: ")
    name = input("Nhập tên cuốn sách: ")
    author = input("Nhập tên tác giả : ")
    release_year = input("Nhập năm xuất bản: ")

    new_book = {
        "id": book_id,
        "name": name,
        "author": author,
        "release_year": release_year,
    }

    with open("info_book.json", 'r+') as file:
        lst_book = json.load(file)
        lst_book.append(new_book)
        json.dump(lst_book, file, indent=4)

    print("Thêm thành công!")
    prevs.add(book_id)


def show_book(book):
    print(f"Id: {book['id']}")
    print(
        f"Name: {book['name']} - Author: {book['author']}- Release_year: {book['release_year']}")


def show_all_book():
    with open('info_book.json', 'r') as file:
        lst_book = json.load(file)
    if lst_book:
        for idx, book in enumerate(lst_book, start=1):
            print(f"Vị trí: {idx}")
            show_book()
    else:
        print("Danh sách trống!")


def find_book():
    with open('info_book.json', 'r') as file:
        lst_book = json.load(file)
    if lst_book:
        book_id = input("Nhập id cuốn sách muốn tìm: ")
        for book in lst_book:
            if book['id'] == book_id:
                show_book()
                break
        else:
            print(f"Không tìm thấy sách có id la: {book_id}")
    else:
        print("Danh sách trống!")


def delete_book(): 
    with open('info_book.json', 'r+') as file:
        lst_book = json.load(file)
    if lst_book:
        book_id = input("Nhập id cuốn sách muốn tìm: ")
        for book in lst_book:
            if book['id'] == book_id:
                lst_book = [b for b in lst if book['id'] != book_id ]
                json.dump(lst_book, file, indent=4)
                break
        else:
            print(f"Không tìm thấy sách có id la: {book_id}")
    else:
        print("Danh sách trống!")

choose = { 
    'a' : add_book,
    'd' : show_all_book,
    'r' : delete_book, 
    'f' : find_book 
}

while True: 
    user_choice = input(USER_MENU)

    if user_choice in choose: 
        do = choose[user_choice]
        do()
    elif user_choice == 'q':
            break
    else: 
        print("Lựa chọn không hợp lệ, vui lòng nhập lại yêu cầu")
        user_choice = input(USER_MENU)