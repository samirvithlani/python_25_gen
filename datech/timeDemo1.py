import time

start = time.perf_counter()
total = sum(range(1_000_000_00))
end = time.perf_counter()
print(total)
print("time..",end-start)