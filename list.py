voltage = [2.4, 3.1, 2.8, 4.0]
voltage.append(3.5)

print("n     =", len(voltage))
print("first =", voltage[0], " last =", voltage[-1])
print(f"mean  = {sum(voltage) / len(voltage):.3f} V")
print("min   =", min(voltage), " max =", max(voltage))

for i, v in enumerate(voltage):
    print(f"V[{i}] = {v:.1f}")