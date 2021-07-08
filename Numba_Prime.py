from numba import jit,njit
import numpy as np
import time

num = int(input('Please enter a number'))

@jit(nopython = True)
def prime(num):
    c = 0
    for i in range(2,(num//2)+1):
        if num%i == 0:
            c += 1
            break

    if c !=0:
        print('Not a Prime')
    else:
        print('Prime')
start = time.time()
prime(num)
end = time.time()
print(f'Time Taken: {end-start}')