from decimal import *
import math
def race(v1, v2, g):
    # your code
    time = Decimal(float(g) / (v1-v2))
    real_time = abs(round(time, 5))
    dec1,int1=math.modf(real_time)
    hour=int(int1)
    x=(dec1*60)
    dec2,int2 = math.modf(x)
    minute = int(int2)
    y=(dec2*60)
    dec3,int3 = math.modf(y)
    second = int(int3)
    return None if v1>=v2 else [hour,minute,second]
