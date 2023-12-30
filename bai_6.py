"""
6.Viết hàm số trả về phân số tối giản của một phân số đầu vào.
"""

#sử dụng thuật toán Euclid để tìm ước chung lớn nhất của hai số a và b.
#Thuật toán Euclid sử dụng việc lặp lại việc chia lấy dư cho đến khi số
# dư là 0. Khi số dư là 0, số chia cuối cùng chính là ước chung lớn nhất của hai số ban đầu.
def uoc_chung_lon_nhat(a, b):
    while b:
        a, b = b, a % b
    return a

#ប្រភាគសម្រួលរួច
def phan_so_toi_gian(tu_so,mau_so):
    tu_so = int(tu_so)
    mau_so = int(mau_so)
    ucln = uoc_chung_lon_nhat(tu_so,mau_so) 
    tu_so_toi_gian = tu_so // ucln
    mau_so_toi_gian = mau_so // ucln
    return tu_so_toi_gian , mau_so_toi_gian

tu_so_nhap = input("Nhập tử số: ")
mau_so_nhap = input("Nhập mẫu số: ")
ketqua_tu_so, ketqua_mau_so = phan_so_toi_gian(tu_so_nhap, mau_so_nhap)
print("Kết quả phân số tối giản là:", ketqua_tu_so, "/", ketqua_mau_so)

