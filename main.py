# timeit
# se masoara durata de executie a codului
# performance chek

# 1, 1, 2, 3, 5, , 8

from time import perf_counter

def fibonacci_recurent(n):
    if not isinstance(n, int) or n <= 0:
        return None
    if n in (1, 2):
        return 1
    return fibonacci_recurent(n - 1) + fibonacci_recurent(n - 2)

time_start = perf_counter()
nth = 36
nth_element = fibonacci_recurent(nth)
print(f"The {nth} element of fb_rec equals = {nth_element}")

print(f"Took = {perf_counter() - time_start}")