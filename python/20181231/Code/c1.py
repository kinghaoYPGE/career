# S = pi*ri^2

"""
ri_1 = 3
ri_2 = 4
ri_3 = 2.1

s1 = 3.14 * ri_1 ** 2
s2 = 3.14 * ri_3 ** 2
s3 = 3.14 * ri_3 ** 2
"""
import math

def get_circle_area(*ri):
    """for r in ri:
        area =math.pi * r ** 2
        area_list.append(area)"""
    # 列表推导式
    
    return [math.pi * r ** 2 for r in ri]







