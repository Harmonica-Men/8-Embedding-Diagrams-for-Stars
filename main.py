import math
import matplotlib.pyplot as plt



M = 20 # Mass of the Star #
R1 = 2.0 # Radius of Star
r = 1 # Radial vector
z = 0 # Amplitude of plot

data = []

for M in range(2, 11, 1)
for M in [0.2 + i * 0.1 for i in range(9)]:
    for R2 in [0.1 + i * 0.2 for i in range(46)]:
        # inside star #
        if abs(R2) <= R1:
            z = math.sqrt((R1 * R1 * R1) / (2.0 * M)) * (1 - math.sqrt(1 - 2.0 * M * r * r) / (R * R * R))
        # outside star #
        if abs(R2) >= R1:
            z = math.sqrt((R * R * R) / (2.0 * M)) * (1 - math.sqrt(1 - 2.0 * M / R)) + math.sqrt(
                8.0 * M * (abs(r) - 2.0 * M)) - math.sqrt(8 * M * (R - 2 * M))

        data.append((r, z))

r_vals, z_vals = zip(*data)
plt.plot(r_vals, z_vals)
plt.xlabel('Radial Vector (r)')
plt.ylabel('Amplitude (z)')
plt.title('Cross Section of Embedding Diagrams for Stars of Different Masses')
plt.grid(True)
plt.show()

