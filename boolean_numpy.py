import numpy as np

T = np.array([29.5, 30.2, 28.9, 31.1, 30.0, 19.4, 33.0])

high = T > 30.0
print("mask       :", high)
print("above 30 C :", T[high])
print("count      :", np.count_nonzero(high))
print(f"percentage : {100 * np.mean(high):.1f} %")

outside = (T < 20.0) | (T > 30.0)
print("outside 20-30 C:", T[outside])