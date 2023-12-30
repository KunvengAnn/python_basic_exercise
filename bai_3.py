"""
3.Viết một hàm số python có tham số đầu vào là 1 danh sách và các giá trị muốn xóa
khỏi danh sách đó. Kết quả đầu ra là 1 danh sách đã được xóa đi các giá trị nhập
vào. Ví dụ: Truyền vào inlist = [5, 8, 11, 9, 11, 8, 8] và giá trị cần xóa là 8 và 11, thì
danh sách đầu ra thu được sẽ là: outlist = [5, 9].
"""
def danhSachDaXao(inputls,inputSocanxoa):
    outputls = []
    for i in inputls: 
        outputls.append(i)   
        
    for soxoa in inputSocanxoa:
        while soxoa in outputls:
            outputls.remove(soxoa)
    return outputls

def timsodaXoa():
    so_cua_ls = input("Nhap danh sach voi cach nhau bang space:").split()
    print("danh sach",list(map(int, so_cua_ls)))
    so_canXoa = input("Nhap so ban muon xoa :").split()
    if(len(so_cua_ls)==0):
        print("danh sach bi rong ko co gi ban ko nhap roi!!")
    else:
        try:
            So_canXoa = list(map(int,so_canXoa))
            So_cua_ls = list(map(int,so_cua_ls))
            ketQua = danhSachDaXao(So_cua_ls,So_canXoa)
            print("danh sach da xoa la:",ketQua)
        except:
            print("vui long nhap so thuc nhe!!")
            
#main
timsodaXoa()
