USER_MENU = ''' Nhập 
    a - Thêm một bộ phim mới 
    s - Hiển thị danh sách phim 
    f - Tìm kiếm các bộ phim theo tên
    d - Xóa phim theo tên
    u - Cập nhật thông tin phim
    q - Thoát   
    Lựa chọn của bạn: '''

movies = []

movies_prevs = set()


def add_movie():
    name = input("Nhập vào tên bộ phim: ")
    while name in movies_prevs:
        print("Phim bị trùng! yêu cầu nhập lại!")
        name = input("Nhập vào tên bộ phim: ")
    diretor = input("Nhập vào tên đạo diễn: ")
    release_year = input("Nhập vào năm phát hành: ")
    movie = {
        "name": name,
        "diretor": diretor,
        "release_year": release_year,
    }
    movies.append(movie)
    movies_prevs.add(name)


def show_movie(movie):
    movie_name = movie['name']
    movie_diretor = movie['diretor']
    movie_release_year = movie['release_year']

    print(f"Tên phim: {movie_name}")
    print(f'Đạo diễn: {movie_diretor}')
    print(f'Năm phát hành: {movie_release_year}')


def show_movies():
    if movies:
        for idx, movie in enumerate(movies, start=1):
            print(f'THÔNG TIN BỘ PHIM: {idx}')
            show_movie(movie)
    else:
        print("Danh sách phim trống")


def find_movie():
    if movies:
        movie_name = input("Nhập vào tên phim cần tìm: ")
        for idx, movie in enumerate(movies, start=1):
            if movie['name'] == movie_name:
                print("THÔNG TIN BỘ PHIM: ")
                print("Vị trí:", idx)
                show_movie(movie)
                break
        else:
            print("Không tìm thấy phim", movie_name)
    else:
        print("Danh sách phim trống")


def delete_movie():
    if movies:
        movie_name = input("Nhập tên phim muốn xóa: ")
        for idx, movie in enumerate(movies, start=1):
            if movie['name'] == movie_name:
                del movies[idx]
                print("Đã xóa phim thành công")
                break
        else:
            print("Không tìm thấy phim", movie_name)
    else:
        print("Danh sách phim trống")


def update_movie():
    if movies:
        movie_name = input("Nhập vào phim muốn cập nhật nội dung: ")
        founds = [
            idx
            for idx, movie in enumerate(movies)
            if movie['name'] == movie_name
        ]
        if founds:
            potision = founds[0]
            movies[potision]['diretor'] = input("Nhập vào tên đạo diễn: ")
            movies[potision]['release_year'] = input("Nhập vào năm phát hành")
            print("Cập nhật thành công thông tin cho phim ", movie_name)
        else:
            print("Không có phim tên", movie_name)
    else:
        print("Danh sách phim trống")


user_choice = input(USER_MENU)

operations = {
    'a': add_movie,
    's': show_movies,
    'f': find_movie,
    'd': delete_movie,
    'u': update_movie,
}

while user_choice != 'q':
    if user_choice in operations: 
        operation = operations[user_choice]
        operation()
    else: 
        print("Yêu cầu không hợp lê, vui lòng nhập lại yêu cầu")
    user_choice = input(USER_MENU)