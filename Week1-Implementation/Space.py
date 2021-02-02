# Authors: @Marthely237 & @luckyjohn-rwanda & @IreneMutamuliza
#Question 2

import memory_profiler
from memory_profiler import profile

@profile (precision=4)
def func():
    a = int(150) * (100-25)
    print(a)

func()
space = memory_profiler.memory_usage()
print(space[-1])
