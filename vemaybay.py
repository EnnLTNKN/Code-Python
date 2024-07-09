
class Vemaybay:
    def __init__(self, tenchuyen, ngaybay, giave):
        self.tenchuyen = tenchuyen
        self.ngaybay = ngaybay
        self.__giave = giave
    
    def nhap(self):
        self.tenchuyen = input("Hãy nhập tên chuyến: ")
        self.ngaybay = input("Hãy nhập ngày bay: ")
        self.giave = int(input("Hãy nhập giá vé: "))
    
    def xuat(self):
        print(f'Tên chuyến: {self.tenchuyen}')
        print(f'Ngày bay: {self.ngaybay}')
        print(f'Giá vé: {self.giave}')
    def getgiave(self):
        return self.__giave
        
class Nguoi:
    def __init__(self, hoten, gioitinh, tuoi):
        self.hoten = hoten
        self.gioitinh = gioitinh
        self.tuoi = tuoi
        
    def nhap(self):
        self.hoten = input("Hãy nhập họ tên: ")
        self.gioitinh = input("Hãy nhập giới tính: ")
        self.tuoi = input("Hãy nhập tuổi: ")
        
    def xuat(self):
        print(f'Họ tên: {self.hoten}')
        print(f'Giới Tính: {self.gioitinh}')
        print(f'Tuổi: {self.tuoi}')
    
class HanhKhach(Nguoi):
    def __init__(self, hoten, gioitinh, tuoi, ve, soluong):
        super().__init__(hoten, gioitinh, tuoi)
        self.ve = ve
        self.soluong = soluong
    
    def nhap(self):
        super().nhap()
        self.soluong = int(input("Nhập số lượng vé: "))
        for i in range (self.soluong):
            print(f'Đang Nhập Thông Tin Vé thứ {i + 1}')
            ve = Vemaybay("", "", "")
            ve.nhap()
            self.ve.append(ve)
            
    def tongtien(self):
        sum = 0
        for i in self.ve:
            sum += i.giave
        return sum
    
    def xuat(self):
        super().xuat()
        print("Thông tin vé máy bay của hành khách: ")
        cnt = 0
        for i in self.ve:
            print(f'Vé thứ {cnt + 1}:')
            i.xuat()
            cnt += 1
        print(f'=> Tổng tiền: {self.tongtien()}')

a = []
n = int(input("Nhập số lượng hành khách: "))
for i in range(n):
    print(f'Nhập thông tin của hành khách thứ {i + 1}:')
    cur = HanhKhach("", "", "", [], "")
    cur.nhap()
    a.append(cur)
    
def comp(x):
    return -x.tongtien()
a.sort(key = comp)

print('THÔNG TIN KHÁCH HÀNG ĐƯỢC SẮP XẾP THEO THỨ TỰ GIẢM DẦN CỦA TỔNG TIỀN: ')
cnt = 1
for i in a:
    print(f'Thông tin của khách hàng thứ {cnt}:')
    i.xuat()
    cnt += 1
    
