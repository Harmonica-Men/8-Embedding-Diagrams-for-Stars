import math

R1 = 2

for M in range(2, 11, 1):
    M /= 10.0  # Convert to floating-point value

    for R2 in [i * 0.2 - 10 for i in range(101)]:  # Equivalent to STEP 0.2 from -10 to 10
        # inside of the star #
        if abs(R2) <= R1:
            Z = math.sqrt((R1 * R1 * R1) / (2 * M)) * (1 - math.sqrt(1 - 2.0 * M * R2 * R2 / (R1 * R1 * R1)))
        else:
            Z = math.sqrt((R1 * R1 * R1) / (2 * M)) * (1 - math.sqrt(1 - 2 * M / R1)) + math.sqrt(8 * M * (abs(R2) - 2.0 * M)) - math.sqrt(8 * M * (R1 - 2.0 * M))

        print(R2, Z)
