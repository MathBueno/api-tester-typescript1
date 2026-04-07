import random
import time

print("Starting tank monitoring...\n")

for i in range(10):
    pressure = random.uniform(0.8, 1.5)
    temperature = random.uniform(20, 80)

    print(f"[Reading {i+1}] Pressure={pressure:.2f} bar | Temp={temperature:.1f}°C")

    if pressure > 1.3:
        print(" ALERT: High pressure!")

    if temperature > 70:
        print(" ALERT: High temperature!")

    print("-" * 40)
    time.sleep(1)
