import numpy as np
from scipy.optimize import linprog

c = np.array([1, 2, 3]) #目标函数
A_ub = np.array([[-2, 1, 1],[3, -1, -2]]) # 不等式约束条件 要求 <= x
b_ub = np.array([9, -4]) #不等式约束的 b
A_eq = np.array([[3, -2, -3]]) #等式的约束条件
b_eq = np.array([-6]) #等式约束的 b

# 最小化求解

#r = linprog(c,A_up,b_up,A_eq,b_eq,bounds = ((None,0),(0,None),(None,None)))
r = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds=((None, 0), (0, None), (None, None)))
print(r)