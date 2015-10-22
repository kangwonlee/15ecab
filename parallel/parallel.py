import multiprocessing as mp
import time
import random


def f(character):
    print time.clock(), character
    return time.clock(), ord(character), ord(character) ** random.randint(1, 256)


if "__main__" == __name__:
    n_core = mp.cpu_count()

    print "number of CPU cores =", n_core

    pool = mp.Pool(n_core)

    pool_map_argument = list('abcdefghijklmnopqrstuvwxyz')

    print time.clock(), "pool_map_argument =", pool_map_argument

    result = pool.map(f, pool_map_argument)
    print time.clock(), "finished pool.map()"

    print time.clock(), result
