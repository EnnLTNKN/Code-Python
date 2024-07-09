def comp(a):
    return a.lop

class sinhvien:
    def __init__(self, masinhvien, ten, lop, gmail):
        self.masinhvien = masinhvien
        self.ten = ten
        self.lop = lop
        self.gmail = gmail
    def xuat(self):
        print(f'{self.masinhvien} {self.ten} {self.lop} {self.gmail}')

a = []
cnt = 0
while (1):

    print("Bạn có muốn thêm sinh viên vào danh sách? [Y/N]")
    t = input() 
    if (t == 'Y'):
        print(f'ĐANG NHẬP THÔNG TIN CHO HỌC SINH THỨ {cnt + 1}')
        print('Mã sinh viên: ')
        masinhvien = input()
        print('Tên: ')
        ten = input()
        print('Lớp: ')
        lop = input()
        print('Gmail: ')
        gmail = input()
        a.append(sinhvien(masinhvien, ten, lop, gmail))
    else:
        print("Kết thúc thêm sinh viên vào danh sách")
        break
    cnt += 1
    
while (1):
    print("Bạn muốn xem danh sách học sinh của lớp nào ? ")
    lop = input()
    print("Danh sách học sinh lớp" ,lop, ":")
    for i in a:
        if (i.lop == lop):
            i.xuat()
    print("Bạn có muốn tiếp tục không ? [Y/N]")
    t = input()
    if t == 'N':
        print("Chương trình đã kết thúc!")
        break