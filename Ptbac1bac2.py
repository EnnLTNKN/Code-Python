import math
class ptbac1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def nhap(self):
        self.a, self.b = map(float, input().split())

    def giaipt(self):
        if self.a == 0:
            if self.b == 0:
                print("Phương trình vô số nghiệm!")
            else:
                print("Phương trình vô nghiệm!")
        else:
            print(f'Phương trình có nghiệm x = {-self.b / self.a}')
    def xuatpt(self):
        print(f'{self.a}x + ({self.b}) = 0 =>', end = " ")
        self.giaipt()

class ptbac2:
    def __init__(self):
        self.hesoa = 0
        self.ptb1 = ptbac1(0, 0)
        
    def nhap(self):
        a, b, c = map(float, input().split())
        self.hesoa = a
        self.ptb1 = ptbac1(b, c)
    def giaipt(self):
        hesoa = self.hesoa
        ptb1 = self.ptb1
        if hesoa == 0:
            ptb1.giaipt()
        else:
            delta = ptb1.a * ptb1.a - 4 * ptb1.b * hesoa
            if delta < 0:
                print("Phương trình vô nghiệm")
            elif delta == 0:
                print(f'Phương trình có một nghiệm kép x = {-ptb1.a / (2 * hesoa)}')
            else:
                print(f'Phương trình có hai nghiệm phân biệt: x1 = {(-ptb1.a - math.sqrt(delta)) / (2 * hesoa)} và x2 = {(-ptb1.a + math.sqrt(delta)) / (2 * hesoa)}')
                
    def xuatpt(self):
        a = self.hesoa 
        b = self.ptb1.a
        c = self.ptb1.b

        print(f'{a}x ^ 2 + ({b})y + ({c}) = 0 => ', end = " ")
        self.giaipt()
    
while 1:
    print("Nhập phương trình bạn muốn giải: ")
    print("1. ax + b = 0")
    print("2. ax ^ 2 + bx + c = 0")
    print("3. Kết thúc")
    
    t = int(input())
    if (t == 1):
        print("Mời bạn nhập các hệ số a, b của phương trình ax + b = 0: ")
        a = ptbac1(1, 1)
        a.nhap()
        a.xuatpt()
    if (t == 2):
        print("Mời bạn nhập các hệ số a, b, c của phương trình ax ^ 2 + bx + c = 0: ")
        a = ptbac2()
        a.nhap()
        a.xuatpt()
    
    if (t == 3):
        print("Chương trình đã kết thúc!")
        break
    
    print("Bạn có muốn tiếp tục không [Y/N]")
    c = input()
    if c == 'N':
        print("Chương trình đã kết thúc!")
        break
        
        

        
