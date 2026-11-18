x0, v0, a = 2.0, 5.0, 3.0      # m, m/s, m/s^2

print(" t(s)    x(m)")
for t in range(0, 6):
    x = x0 + v0 * t + 0.5 * a * t**2
    print(f"{t:4d} {x:8.2f}")

# metode Babilonia dengan while
s, x, tol = 2.0, 1.0, 1e-12
iterations = 0
while True:
    x_new = 0.5 * (x + s / x)
    iterations += 1
    if abs(x_new - x) < tol or iterations >= 100:
        break
    x = x_new
print(f"sqrt(2) ~= {x_new:.15f} after {iterations} iterations")