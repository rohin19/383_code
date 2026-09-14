import time
from pathlib import Path

def for_loop_sol():
    start_time = time.time()
    list = []
    with open("../python/python_sum/numbers.txt") as numbers:
        for line in numbers:
            n = int(line)
            if 1 <= n <= 100:
                list.append(n)

    sum = 0
    for n in list:
        sum += n
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
    print(sum)


for_loop_sol()