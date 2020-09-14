from CalculatorsScripts.ExEvclid import FindExEvclid
class Diophantine:
    a = 0
    ifAneg = 1
    b = 0
    ifBneg = 1
    c = 0
    resEvclid = []
    x0 = 0
    y0 = 0
    toEnlarge = 1
    x = []
    y = []
    solved = True
    def __init__(self, c):
        self.c = c
        self.x = []
        self.y = []



def DiophaniteRight(a, b ,c ,tBegin, tEnd):
    #todo для отрицательных входных считает неправильно
    CurrentAnswer = Diophantine(c)
    CurrentAnswer.a = a
    if (a<0):
        CurrentAnswer.ifAneg = -1
    CurrentAnswer.b = b
    if b<0:
        CurrentAnswer.ifBneg = -1
    CurrentAnswer.resEvclid = FindExEvclid(abs(a),abs(b))
    d = CurrentAnswer.resEvclid[-1].r
    u = CurrentAnswer.resEvclid[-1].u
    v = CurrentAnswer.resEvclid[-1].v
    #a*u + b*v = d
    #a*u*(c/d) + b*v(c/d) = c
    if c % d != 0:
        CurrentAnswer.solved = False
    else:
        CurrentAnswer.toEnlarge = int (CurrentAnswer.c / d)
        CurrentAnswer.x0 = u* int(CurrentAnswer.c / d)*CurrentAnswer.ifAneg
        CurrentAnswer.y0 = v * int(CurrentAnswer.c/d)*CurrentAnswer.ifBneg
        #x = x0 + b/d *t
        #y = y0 + b/d *t
        i = tBegin
        while i <= tEnd:
            xCurrent = CurrentAnswer.x0 + CurrentAnswer.b / d * i
            yCurrent = CurrentAnswer.y0 - CurrentAnswer.a /d * i
            CurrentAnswer.x.append(xCurrent)
            CurrentAnswer.y.append(yCurrent)
            i = i + 1;
    return CurrentAnswer










