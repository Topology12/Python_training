movies = []


film = {
    "name": "Tay Du Ki",
    'diretor': "A",
    'release_year': 1990,
}
movies.append(film)

def delete_movie(): 
    global movies
    movie_name = input("Nhap vao film muon xoa: ")
    movies = [tuple(idx, movie) for idx, movie in enumerate(movies, start=1) if movie['name'] != movie_name  ]

delete_movie()
print(movies)