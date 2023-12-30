"""
10.Viết một hàm chuẩn hóa xâu ký tự: biến đổi xâu ký tự nhập vào từ bàn phím thành
xâu chuẩn sao cho trong xâu không có 2 dấu cách liền nhau, chữ cái đầu tiên và sau
dấu cách của chuỗi phải được viết hoa, các chữ cái khác phải viết thường.
Ví dụ: Nhập vào chuỗi: nGuyen VaN A
chuẩn hóa: Nguyen Van A.
"""
def chuan_hoa_xau(xau):
    # Chuyển tất cả các ký tự thành chữ thường
    xau = xau.lower()
    words = xau.split()
    # Chuẩn hóa từng từ trong danh sách từ
    chuan_hoa = [word.capitalize() for word in words]
    # Ghép các từ đã chuẩn hóa với dấu cách giữa các từ
    return ' '.join(chuan_hoa)

xau_nhap = input("Nhập xâu ký tự: ") #nguYEN vaN A
# Chuẩn hóa xâu và in kết quả
xau_chuan_hoa = chuan_hoa_xau(xau_nhap)
print("Xâu ký tự chuẩn hóa:", xau_chuan_hoa)

