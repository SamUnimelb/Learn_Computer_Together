import math
import time

start = time.perf_counter()

x = 0.0
while x <= 10000.0:
    fx = x * math.sin(x)
    x += math.pow(2, -8)

duration = time.perf_counter() - start
print("Time spent: " + str(duration * 10 ** 3) + " milliseconds.")
