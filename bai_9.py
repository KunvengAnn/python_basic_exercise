"""
9.Viết hàm kiểm tra tính đối xứng của 1 xâu ký tự. Sau đó gọi hàm và nhập xâu ký tự
từ bàn phím và cho biết xâu đó có đối xứng không.
"""
def kiem_tra_doi_xung(xau):
    return xau == xau[::-1] #so sach xau ban dau voi xau dao ky tu co giong nhau ko

xau_ky_tu = input("Nhập xâu ký tự: ")

#ABCBA la xau doi xung
if kiem_tra_doi_xung(xau_ky_tu):
    print("Xâu là xâu đối xứng.")
else:
    print("Xâu không đối xứng.")