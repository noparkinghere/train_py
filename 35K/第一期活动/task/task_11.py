"""
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
这是一题比较基础的物理题（设置只能说是数学题），第一次落地经过 10 米，第二次落地经过 10+10/2*2 = 20，等。第一次反弹 10/2 米，第二反弹 10/2/2 米，等。
"""

def rebound(org_height, times):
    total_len = float(org_height)
    rebound_height = float(org_height) / 2.0
    for i in range(1, times):
        total_len += rebound_height
        rebound_height /= 2.0
    return total_len, rebound_height
    
print("一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，在第10次落地时，共经过 %d 米，第10次反弹高度为 %f" % (rebound(100, 10)))