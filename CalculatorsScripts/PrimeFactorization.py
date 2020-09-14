class Answer:
    n = 0
    Ans = 0
    def __init__(self, n ,a):
        self.n = n
        self.Ans = a

def PrimeFactor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(Answer(n,d))
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(Answer(n,n))
    return Ans