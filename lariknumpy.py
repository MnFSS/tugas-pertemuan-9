import numpy as np

t = np.linspace(0.0, 2.0, 21)            # 21 titik, langkah 0.1 s
x = 2.0 + 5.0 * t + 0.5 * 3.0 * t**2     # x(t) = x0 + v0 t + a t^2 / 2

print("number of points:", t.size)
print("t[:4] =", t[:4])
print("x[-1] =", x[-1], "m")
print(f"mean = {x.mean():.3f}, std = {x.std():.3f}, max = {x.max():.3f}")