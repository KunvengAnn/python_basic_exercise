"""
4.Viết một hàm Python để tính toán giai thừa của một số (một số nguyên không âm).
Gợi ý: Sử dụng hàm đệ quy n! = (n-1)!*n.
"""
def tinh_giai_thua_de_quy(n):
    if(n == 0 or n == 1):
        if n == 1:
            print(n, end=' = ')
        return 1
    else:
        print(n, end=' * ')
        return n * tinh_giai_thua_de_quy(n - 1)

so_n = int(input("nhap so nguyen n:"))
if(so_n < 0):
    print("ko tinh duoc vi so nguyen phai > 0")
else:
    print("ket qua tinh giai thua bang de quy", end=' ')
    ketqua = tinh_giai_thua_de_quy(so_n)
    print(ketqua)


#Sử dụng vòng lặp:
# def tinh_giai_thua_vong_lap(n):
#     giai_thua = 1
#     ket_qua = ""
#     for i in range(1, n+1):
#         giai_thua *= i
#         ket_qua += str(i)
#         if i < n:
#             ket_qua += " * "
#     print(f"{ket_qua} = {giai_thua}")
#     return giai_thua
# so_n = int(input("Nhap so nguyen bat ky:"))  # Số nguyên dương nào đó
# ket_qua = tinh_giai_thua_vong_lap(so_n)






