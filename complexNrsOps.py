import math
class nrComplex:
    '''init'''
    def __init__(self, reeal, imm):
        self.__r = reeal
        self.__i = imm
    '''getters'''
    def getReal(self):
        return self.__r
    def getImm(self):
        return self.__i
    '''setters'''
    def setReal(self, newR):
        self.__r = newR
    def setImm(self, newI):
        self.__i = newI
    def printResult(self):
        if self.__i < 0:
            return "The result has the following form: c = "+str(self.__r)+" "+str(self.__i)+"i."
        else:
            return "The result has the following form: c = "+str(self.__r)+" + "+str(self.__i)+"i." 
    '''simple operations with one complex number'''
    def printCartesian(self):
        return "The number's real part is "+str(self.__r) + " and its imaginary part is "+ str(self.__i)
    def printConjugate(self):
        return "The conjugate has its real part of "+str(self.__r)+" and its imaginary part is "+(-1)*str(self.__i)
    def printPolar(self):
        m = math.sqrt(self.__r* self.__r + self.__i*self.__i)
        if m == 0:
            cosphi = 1
            sinphi = 0
        else:
            cosphi = self.__r / m
            sinphi = self.__i/m
        return "The number's polar form is the following: c = "+str(m)+"("+str(cosphi)+" + "+str(sinphi)+"i)."
    def multiplyByReal(self, reCoeff):
        self.__r = self.__r * reCoeff
        self.__i = self.__i * reCoeff
        return nrComplex.printResult(self)
    def multiplyByIm(self, imCoeff):
        self.__i = self.__i * imCoeff * (-1)
        self.__r = self.__r * imCoeff
        inloc = self.__i
        self.__i = self.__r
        self.__r = inloc
        return nrComplex.printResult(self)
    '''operations with two complex numbers'''
    def addTwo(self, other):
        self.__r = self.__r + other.__r
        self.__i = self.__i + other.__i
        return nrComplex.printResult(self)
    def multiplyTwo(self, other):
        self.__r = self.__r * other.__r - self.__i * other.__i
        self.__i = self.__r * other.__i + self.__i * other.__r
        return nrComplex.printResult(self)
    '''complex operations with one complex number'''
    def matrixForm(self):
        #mat = [[self.__r, -self.__i], [self.__i, self.__a]]
        return str(self.__r)+' -'+str(self.__i)+'\n'+str(self.__i)+' '+str(self.__r)
    def powNumber(self, newPow):
        while newPow > 0:
            nrComplex.multiplyTwo(self, self)
            newPow = newPow - 1
        return nrComplex.printResult(self)
    def sqrtNumber(self):
        m = math.sqrt(self.__r* self.__r + self.__i*self.__i) #modulus of the number
        if self.__r == 0:
            phi = math.pi / 4
        else:
            phi = math.atan(self.__i/self.__r)*180/math.pi
        m = math.sqrt(m)
        return "The result is c = "+str(m)+"(cos("+str(phi/2)+")+ isin("+str(phi/2)+"))."
    def expNumber(self):
        #e^(a + ib) = e^a* (e^ib)
        #e^ib = cosb + isinb
        self.__r = math.exp(self.__r)*math.cos(self.__i)
        self.__i = math.exp(self.__r)*math.sin(self.__i)
        return nrComplex.printResult(self)
'''Tests'''
   
def test_printCartesian():
    assert nrComplex.printCartesian(1, 0) == "The number's real part is 1 and its imaginary part is 0"
    assert nrComplex.printCartesian(-1, 3) == "The number's real part is -1 and its imaginary part is 3"

def test_printConjugate():
    assert nrComplex.printConjugate(1, 3) == "The conjugate has its real part of 1 and its imaginary part is -3"
    assert nrComplex.printConjugate(0, 0) == "The conjugate has its real part of 0 and its imaginary part is 0"
    assert nrComplex.printConjugate(-5, -5) == "The conjugate has its real part of -5 and its imaginary part is 5"
    
def test_printPolar():
    assert nrComplex.printPolar(1, 1) == "The number's polar form is the following: c = 1.41421356237(0.707106781187 + 0.707106781187i)"
    assert nrComplex.printPolar(1, 0) == "The number's polar form is the following: c = 1.0(1.0 + 0.0i)"
    assert nrComplex.printPolar(0,0) == "The number's polar form is the following: c = 0.0(1 + 0i)"
    
def test_multiplyByRe():
    assert nrComplex.multiplyByReal(1, 1, 3) == "The result has the following form: c = 3 + 3i."
    assert nrComplex.multiplyByReal(3, 3, 0) == "The result has the following form: c = 0 + 0i."
    assert nrComplex.multiplyByReal(1, -1, -1) == "The result has the following form: c = -1 + 1i."
    assert nrComplex.multiplyByReal(1, 1, -1) == "The result has the following form: c = -1 -1i."

def test_multiplyByIm():
    assert nrComplex.multiplyByIm(2, 1, 1) == "The result has the following form: c = -1 + 2i."
    assert nrComplex.multiplyByIm(3, -1, 2) == "The result has the following form: c = 2 + 6i."
    assert nrComplex.multiplyByIm(1, 1, 0) == "The result has the following form: c = 0 + 0i."
    assert nrComplex.multiplyByIm(0, 1, 3) == "The result has the following form: c = -3 + 0i."
    
def test_addTwo():
    assert nrComplex.addTwo(1, 2, 2, 1) == "The result has the following form: c = 3 + 3i."
    assert nrComplex.addTwo(-1, 3, 1, -3) == "The result has the following form: c = 0 + 0i."
    assert nrComplex.addTwo(0, 0, 0, 0) == "The result has the following form: c = 0 + 0i."
    assert nrComplex.addTwo(3, 2, 5, 1) == "The result has the following form: c = 8 + 3i."
    
def test_MultiplyTwo():
    assert nrComplex.multiplyTwo(1, 1, 1, 0) == "The result has the following form: c = 1 + 1i."
    assert nrComplex.multiplyTwo(0, 1, 0, 1) == "The result has the following form: c = -1 + 0i."
    assert nrComplex.multiplyTwo(4, 3, 1, 2) == "The result has the following form: c = -2 + 11i."
    assert nrComplex.multiplyTwo(1, 2, 2, 1) == "The result has the following form: c = 0 + 5i."

def test_powNbr():
    assert nrComplex.powNumber(1, 0, 3) == "The result has the following form: c = 1 + 0i."
    assert nrComplex.powNumber(0, 1, 4) == "The result has the following form: c = 1 + 0i."
    assert nrComplex.powNumber(1, 1, 2) == "The result has the following form: c = 0 + 2i."
    assert nrComplex.powNumber(1, 2, 3) == "The result has the following form: c = -11 -2i."
    assert nrComplex.powNumber(0, 0, 5) == "The result has the following form: c = 0 + 0i."

def test_sqrtNbr():
    assert nrComplex.sqrtNumber(1, 0) == "The result is c = 1.0(cos(0.0)+ isin(0.0))."
    assert nrComplex.sqrtNumber(-4, 0) == "The result is c = 2.0(cos(0.0)+ isin(0.0))."

def test_expNbr():
    assert nrComplex.expNumber(1, 1) == "The result has the following form: c = 1.46869393992 + 3.65497843719i."
    assert nrComplex.expNumber(0, 0) == "The result has the following form: c = 1.0 + 0.0i."
    assert nrComplex.expNumber(1, 0) == "The result has the following form: c = 2.71828182846 + 0.0i."
    assert nrComplex.expNumber(0, 1) == "The result has the following form: c = 0.540302305868 + 1.44440657085i."

def test_all():
    try:
        test_printCartesian()
    except:
        "There's something wrong with the cartesian function!"
    try:
        test_printConjugate()
    except:
        "There's something wrong with the conjugate function!"
    try:
        test_printPolar()
    except:
        "There's something wrong with the polar print function!"
    try:
        test_multiplyByRe()
    except:
        "There's something wrong with the multiplyByReal function!"
    try:
        test_multiplyByIm()
    except:
        "There's something wrong with the multiplyByIm function!"
    try:
        test_addTwo()
    except:
        "There's something wrong with the addTwo function!"
    try:
        test_MultiplyTwo()
    except:
        "There's something wrong with the multiplyTwo function!"
    try:
        test_powNbr()
    except:
        "There's something wrong with the powNbr function!"
    try:
        test_sqrtNbr()
    except: 
        "There's something wrong with the sqrtNumber function!"
    try:
        test_expNbr()
    except:
        "There's something wrong with the expNbr function!"
    
        
test_all()
'''UI'''
    
print "Hi! Thanks for dropping by. Here you'll be able to do a lot of stuff with, you guessed it, complex numbers!"
print "You'll need to press the following numbers for their corresponding actions:"
print "1 - See the Cartesian form of the number you input!\t\t\t2 - See the Conjugate of the number you input!"
print "3 - See the Polar form of the number you input!\t\t\t\t4 - Multiply your number by a real number!"
print "5 - Multiply your number with a imaginary number!\t\t\t6 - Add two complex numbers!"
print "7 - Multiply two complex numbers!\t\t\t\t\t8 - See a number in its matrix form!"
print "9 - See the number you input to a power n!\t\t\t\t10 - See the square root of the number you input!"
print "11 - See the exponential of the number you input!"
print "If you don't want to do one of the beforementioned actions, feel free to press 0. Have fun!"
a = int(raw_input("Please input the real part of the number!"))
b = int(raw_input("Please input the imaginary part of the number!"))
numar = nrComplex(a, b)
while 1:
    choice = int(raw_input("So, what do you want to do?"))
    if choice == 1:
        print nrComplex.printCartesian(numar)
    elif choice == 2:
        print nrComplex.printConjugate(numar)
    elif choice == 3:
        print nrComplex.printPolar(numar)
    elif choice == 4:
        reAl = int(raw_input("Hi! Please input the real number!"))
        print nrComplex.multiplyByReal(numar, reAl)
    elif choice == 5:
        imAg = int(raw_input("Hi! Please input the imaginary coefficient!"))
        print nrComplex.multiplyByIm(numar, imAg)
    elif choice == 6:
        c = int(raw_input("Hi! Please input the real part of the second number!"))
        d = int(raw_input("Hi! Please input the imaginary coefficient of the second number!"))
        numarDoi = nrComplex(c, d)
        print nrComplex.addTwo(numar, numarDoi)
    elif choice == 7:
        c = int(raw_input("Hi! Please input the real part of the second number!"))
        d = int(raw_input("Hi! Please input the imaginary coefficient of the second number!"))
        numarDoi = nrComplex(c, d)
        print nrComplex.multiplyTwo(numar, numarDoi)
    elif choice == 8:
        print nrComplex.matrixForm(numar)
    elif choice == 9:
        putere = int(raw_input("Hi! To what power do you want to raise the complex number?"))
        print nrComplex.powNumber(numar, putere)
    elif choice == 10:
        print nrComplex.sqrtNumber(numar)
    elif choice == 11:
        print nrComplex.expNumber(numar)
    elif choice == 0:
        print "See you soon!"
        exit()
    else:
        print "Please input a number between 0 and 11!"