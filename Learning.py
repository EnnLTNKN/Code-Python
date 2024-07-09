# class NguoiVietNam:
#     def chay(self):
#         print('đang chạy')
#     def ngu(self):
#         print('đang ngủ')
        
# nguoi1 = NguoiVietNam()
# nguoi1.cao = 1.8
# nguoi1.nang = 80
## => Cao và nặng là hai thành phần của riêng người 1 không phải của class

# class NguoiVietNam:
#     def __init__(self, cao, nang):
#         self.cao = cao
#         self.nang = nang
#     # cao và nặng là hai thành phần của class NguoiVietNam => khởi tạo constructor
#     def chay(self):
#         print('đang chạy')
#     def ngu(self):
#         print('đang ngủ')

# nguoi1 = NguoiVietNam(1.8, 70)
# nguoi2 = NguoiVietNam(1.9, 85)

# class sinhvien:
#     def __init__(self, ten, lop, gpa):
#         self.ten = ten
#         self.lop = lop
#         self.gpa = gpa
    
# a = sinhvien(input(), input(), input())
# print(a.ten, a.lop, a.gpa)

#Getter, setter, deleter

class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    @property
    def fullname(self):
        return f'{self.brand} {self.model}'
    
    @fullname.setter
    def fullname(self, fullname):
        self.brand, self.model = fullname.split(" ")
    @fullname.deleter
    def fullname(self):
        self.brand = None
        self.model = None
        print('Deleted fullname')

car1 = car("Vinfast", "Lux A 2.0")
car1.fullname = "BMW i320"
del car1.fullname
print(car1.brand, car1.model)

# Tính trừu tượng: Vật ngoài đời -> trừu tượng hóa thành một class gồm thuộc tính và phương thức
# Tính đóng gói: Access modifier => setPrivate dùng __. Ví dụ: model -> __model
# Tính đa hình: Cùng một tên hàm nhưng những class con có thể có những hàm khác nhau