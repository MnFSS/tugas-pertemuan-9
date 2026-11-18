import belajar_numpy as np

mass = np.array([1.0, 2.0, 3.0, 4.0])        # kg
velocity = np.array([2.0, 3.0, 1.5, 0.5])    # m/s

energy = 0.5 * mass * velocity**2             # tanpa loop
print("E       =", energy)
print("E_total =", energy.sum(), "J")

# perbandingan: list biasa memerlukan loop
energy_list = [0.5 * m * v**2 for m, v in zip([1.0, 2.0, 3.0, 4.0], [2.0, 3.0, 1.5, 0.5])]
print("list    =", energy_list)