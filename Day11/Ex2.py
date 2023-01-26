# Định nghĩa một hàm được gọi là print_show_info nhận vào một tham số duy nhất và in thông tin của dict tv_show
def print_show_info(info):
    print(
        f"{info['title']} ({info['initial_release']}) - {info['seasons']} seasons")


tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}
print_show_info(tv_show)
