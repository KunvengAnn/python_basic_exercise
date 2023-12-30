"""
7.Viết hàm số tìm và in ra phần tử nhỏ nhất, lớn nhất, tính và in ra trung bình cộng
của các phần tử trong danh sách hoặc tuple cho trước. In ra các phần tử nhỏ hơn,
lớn hơn trung bình cộng.
"""
def thong_tin_danh_sach(danhsach):
    if not danhsach:
        print("Danh sach hoac tuple ko co gi ! trong")
        return
    else:
        max_value = max(danhsach)
        min_value = min(danhsach)
        so_phan_tu_danhsach = len(danhsach)
        average = sum(danhsach) / so_phan_tu_danhsach
        
        print("Phần tử nhỏ nhất:", min_value)
        print("Phần tử lớn nhất:", max_value)
        print("Trung bình cộng:", average)

        print("+ Các phần tử nhỏ hơn trung bình cộng:")
        for item in danhsach :
            if(item < average):
                print(item, end=' ')
        print("\n+ Các phần tử lớn hơn trung bình cộng:")
        for item in danhsach:
            if(item > average):
                print(item,end=' ')
            
# Danh sách bạn muốn sử dụng
danh_sach = [2, 5, 8, 12, 4, 10]

thong_tin_danh_sach(danh_sach)