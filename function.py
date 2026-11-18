def kinetic_energy(mass, velocity):
    """Energi kinetik (J) dari massa (kg) dan kecepatan (m/s)."""
    return 0.5 * mass * velocity**2

def momentum(mass, velocity):
    return mass * velocity

print(f"E = {kinetic_energy(2.0, 3.0):.3f} J")
print(f"p = {momentum(2.0, 3.0):.3f} kg m/s")