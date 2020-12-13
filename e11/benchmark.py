import timeit
import ex_1
import ex_2


def do_both():
    ex_1.doit(False)
    ex_2.doit(False)

#print(timeit.timeit(do_both, number=1) * 1000, "ms")
print(timeit.timeit(do_both, number=100) / 100 * 1000, "ms")
