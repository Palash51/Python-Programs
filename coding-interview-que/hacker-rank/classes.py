import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        rSum = self.real + no.real
        iSum = self.imaginary + no.imaginary
        import pdb
        pdb.set_trace()

        return Complex(rSum, iSum)
        
    def __sub__(self, no):
        rSub = self.real - no.real
        iSub = self.imaginary - no.imaginary
        return Complex(rSub, iSub)
        
    def __mul__(self, no):
        rmul = self.real * no.real + self.imaginary*no.imaginary*(-1)
        imul = self.real * no.imaginary + self.imaginary*no.real
        return Complex(rmul, imul)

    def __truediv__(self, no):
        conjucation = Complex(no.real, no.imaginary*(-1))
        num = self*conjucation
        denom = no*conjucation
        rQuo = num.real/denom.real
        iQuo = num.imaginary/denom.real
        return Complex(rQuo, iQuo)

    def mod(self):
        m = math.pow(math.pow(self.real,2) + math.pow(self.imaginary,2), 0.5)
        return Complex(m, 0)


    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')