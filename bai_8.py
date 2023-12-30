"""
8.Viết hàm đếm số các đoạn tăng và tìm đoạn tăng dài nhất của một danh sách cho
trước. Sau đó in ra kết quả số đoạn tăng và đoạn tăng dài nhất trong danh sách.
"""
def dem_duong_tang(danh_sach):
    dem = 1
    dem_max = 1
    doan_tang_max = []

    for i in range(len(danh_sach) - 1):
        if danh_sach[i] < danh_sach[i + 1]:
            dem += 1
        else:
            if dem > dem_max:
                dem_max = dem
                doan_tang_max = danh_sach[i - dem_max + 1: i + 1]
            dem = 1

    if dem > dem_max:
        dem_max = dem
        doan_tang_max = danh_sach[len(danh_sach) - dem_max:]

    return dem_max, doan_tang_max


danh_sach = [1, 2, 3, 2, 4, 6, 8, 9, 3, 4, 5,10,11,20]
dem, doan_tang_max = dem_duong_tang(danh_sach)

print("Số đoạn tăng:", dem)
print("Đoạn tăng dài nhất:", doan_tang_max)

