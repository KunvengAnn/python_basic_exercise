"""
1.Viết hàm số python để tính diện tích hình tròn.
"""

def tim_dien_tich_hinh_tron(r):
    if(r < 0):
        print("ban kinh phai lon hon 0!")
        return 
    else:
        pi = 3.14
        s =r*r*pi
        print("dien tinh hinh tron la:",s)

r = int(input("Nhap ban kinh r: "))
ketqua = tim_dien_tich_hinh_tron(r)
