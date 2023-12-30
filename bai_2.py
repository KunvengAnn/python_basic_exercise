"""
2.Viết một hàm số python có tham số đầu vào là 1 danh sách. Và đầu ra là 1 danh
sách chỉ chứa các số chia hết cho 3 có trong danh sách đầu vào. Ví dụ: Truyền vào
inlist = [3, 6, 8, 11, 9, 16, 21, 22] thì đầu ra là _outlist = [3, 6, 9, 21].
"""
def timlschia3(inputls):
    outputls = [];
    for sochia3 in inputls:
        if(sochia3%3==0):
            outputls.append(sochia3)
    return outputls

#
so_cua_ls =input("Nhap danh sach so nguyen:").split()
if(len(so_cua_ls)==0):
    print("danh sach rong ko co gi!")
else:
    try:
        lsSoChiaBa = list(map(int,so_cua_ls))# phai la so thuc 
        dsSoChiaBa = timlschia3(lsSoChiaBa)
        print("danh sach chia het cho 3 la",dsSoChiaBa) 
    except:
        print("vui long nhap so thuc nhe!")



