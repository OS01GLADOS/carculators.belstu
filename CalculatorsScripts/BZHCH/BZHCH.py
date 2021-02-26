from enum import Enum


def PrimaryCloudMatterAmount(k1, k3, k5, k7, q0):
    return k1*k3*k5*k7*q0

def PressurizedGasAmount(d,Vx):
    return d*Vx

def PipelineGasAmount(n,d,v):
    return (n*d*v)/100

#0-инверсия, 1-изотермимя, 2-конвекция
def k5_get(input):
    if input==0:
        return 1
    elif input ==1:
        return 0.23
    else:
        return 0.08

def TimeOfEvaporation(h,d,k2,k4,k7):
    return (h*d)/(k2*k4*k7)

def h_getSingular(H):
    return  H-0.2

def h_getGroup(q0,F,d):
    return q0/(F*d)






class Table1_1:
    def __init__(self, name, k1, k2, k3, tem1, tem2 ):
        self.name = name
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.TemperatureFirstCloud = Table1_1Temperature(tem1[0],tem1[1],tem1[2],tem1[3],tem1[4])
        self.TemperatureSecondCloud = Table1_1Temperature(tem2[0],tem2[1],tem2[2],tem2[3],tem2[4])
class Table1_1Temperature:
    def getK7(self, Temperature):
        if Temperature == 0.0:
            return self.kZERO
        elif Temperature < 0.0:
            if Temperature > -20.0:
                return (self.kZERO - self.kMINUS20) / 2
            elif Temperature == -20.0:
                return self.kMINUS20
            elif Temperature > -40.0:
                return (self.kMINUS20 - self.kMINUS40) / 2
            else:
                return self.kMINUS40

        elif Temperature > 0:
            if Temperature < 20.0:
                return (self.kPLUS20 - self.kZERO)/2
            elif Temperature == 20.0:
                return self.kPLUS20
            elif Temperature < 40.0:
                return (self.kPLUS40 - self.kPLUS20) / 2
            else:
                return self.kPLUS40
    def __init__(self, t140, t120, t000, t020, t040):
        self.kMINUS40 = t140
        self.kMINUS20 = t120
        self.kZERO = t000
        self.kPLUS20 = t020
        self.kPLUS40 = t040

class Table1_2:
    def __init__(self,name, GasConsistence, LiquidConsistence, BoilingTemperature, SomeFuckingShit):
        self.name = name
        self.GasConsistence = GasConsistence
        self.LiquidConsistence = LiquidConsistence
        self.BoilingTemperature = BoilingTemperature
        self.Toksodoza = SomeFuckingShit

class Table1_3:
    def __init__(self,windSpeed, value):
        self.windSpeed = windSpeed
        self.value = value