class ExEvclid:
  r = 0
  u = 0
  v = 0
  q = -1
  qb= -1
  def __init__(self, u, v, r):
    self.r=r
    self.u=u
    self.v=v

def FindExEvclid(a,b):
  ResArr = []
  ResArr.append(ExEvclid(1,0,a))
  ResArr.append(ExEvclid(0,1,b))
  i=1
  while(ResArr[-1].r!=0):
    ResArr[i].q=int(ResArr[i-1].r/ResArr[i].r)
    ResArr[i].qb = ResArr[i].q * ResArr[i].r
    rNext = ResArr[i-1].r - ResArr[i].q*ResArr[i].r
    vNext = ResArr[i-1].v - ResArr[i].q*ResArr[i].v
    uNext = ResArr[i-1].u - ResArr[i].q*ResArr[i].u
    ResArr.append(ExEvclid(uNext,vNext,rNext))
    i =i+1
  ResArr.pop(-1)
  return ResArr

def GetBigger(a,b):
    res = []
    if a>b:
        res = FindExEvclid(a,b)
    else:
        res =FindExEvclid(b,a)
    return  res