import numpy as np
from scipy.optimize import linprog

c = np.array([1, 2, 3])  # 目标函数的系数
A_ub = np.array([[-2, 1, 1], [3, -1, -2]])  # 不等式约束的A，格式是<=
b_ub = np.array([9, -4])  # 不等式约束的b
A_eq = np.array([[3, -2, -3]])  # 等式约束的A
b_eq = np.array([-6])  # 等式约束的b

# 求解，最小化
r = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds=((None, 0), (0, None), (None, None)))
print(r)