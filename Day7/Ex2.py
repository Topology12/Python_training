# Cho dict sau
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}

# Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
album_name1 = album_info["album_name"]
print(album_name1)
key1 = "album_name"
print(album_info.get(key1))
year = album_info["release_year"]
print(year)
key2 = "release_year"
print(album_info.get(key2))

# Thay đổi release_year từ 1973 thành 1971
album_info.update(release_year=1971)
print(album_info["release_year"])

# Xóa key track_list
album_info.pop("track_list")
print(album_info)

# Thêm key mới amount = 2000
album_info.update(amount='2000')
print(album_info)

# Làm trống dict
album_info.clear()
print(album_info)
