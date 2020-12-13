import timeit
import ex_1
import ex_2


def do_both():
    ex_1.doit()
    ex_2.doit()


print(timeit.timeit(do_both, number=100) / 100 * 1000, "ms")
