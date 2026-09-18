# N -- should be adjusted to a larger number for better accuracy (set to 100000000 for computational capability)
# Written by Takumi S (09.17.2026)
import random

N = 10000000
M = 0

for i in range(N):
    if (random.random()**2) + (random.random()**2) <= 1:
        M += 1

ratio = M / N
estimate_pi = 4 * ratio

print("estimated value of pi:", estimate_pi)