"""
5.Viết hàm số cho phép nhập vào 1 danh sách số nguyên, và trả về giá trị trung bình
của danh sách đó.
"""
def gia_tri_trung_binh(danh_sach):
    tong = sum(danh_sach)
    phan_tu = len(danh_sach)
    if(len(danh_sach)==0):
        return 0  # Trả về 0 nếu danh sách rỗng để tránh lỗi chia cho 0
    return tong / phan_tu

so_ds = input("Nhap danh sach so nguyen: ").split();
if(len(so_ds)<0):
    print("danh sach rong ko co gi!")
else:
    try:
        So_danhsach = list(map(int,so_ds)) # phai la so thuc
        ketqua = gia_tri_trung_binh(So_danhsach)
        print("giá trị trung bình của danh sách: ",ketqua)
    except:
        print("hay nhap so thuc nhe!")



    