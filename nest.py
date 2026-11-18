temperature = float(input("Temperature (C): "))

if temperature < 20:
    status = "DINGIN"
elif temperature <= 30:
    status = "NORMAL"
else:
    status = "PANAS"

print(f"T = {temperature:.1f} C -> {status}")