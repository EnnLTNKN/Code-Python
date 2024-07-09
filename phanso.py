import math
class phanso:
    def __init__(this, tu, mau):
        this.tu = tu
        this.mau = mau
    def rutgon(this):
        x = math.gcd(this.tu, this.mau)
        this.tu /= x
        this.mau /= x
    def xuat(this):
        print(f'{this.tu}/{this.mau}')
    
def cong(a, b):
    t = phanso(a.tu * b.mau + a.mau * b.tu, a.mau * b.mau)
    t.rutgon()
    return t

def tru(a, b):
    t = phanso(a.tu * b.mau - a.mau * b.tu, a.mau * b.mau)
    t.rutgon()
    return t

def nhan(a, b):
    t = phanso(a.tu * b.tu, a.mau * b.mau)
    t.rutgon()
    return t

def chia(a, b):
    t = phanso(a.tu * b.mau, a.mau * b.tu)
    t.rutgon()
    return t

while (1):
    
    print("Mời bạn nhập phân số thứ nhất: (a / b)")
    tu, mau = map(int, input().split())
    a = phanso(tu, mau)
    print("Mời bạn nhập phân số thứ hai: (a / b)")
    tu, mau = map(int, input().split())
    b = phanso(tu, mau)
    
    print("Mời bạn nhập lựa chọn: ")
    print("1. Cộng hai phân số")
    print("2. Trừ hai phân số")
    print("3. Nhân hai phân số")
    print("4. Chia hai phân số")
    print("5. Kết thúc")

    t = int(input())
    if t == 1:
        cong(a, b).xuat()
    if t == 2:
        tru(a, b).xuat()
    if t == 3:
        nhan(a, b).xuat()
    if t == 4: 
        chia(a, b).xuat()
    if (t == 5):
        print("Chương trình đã kết thúc!")
        break
    
    print("Bạn có muốn tiếp tục chứ: [Y/N]")
    c = input()
    if c == 'N':
        print("Chương trình đã kết thúc")
        break

