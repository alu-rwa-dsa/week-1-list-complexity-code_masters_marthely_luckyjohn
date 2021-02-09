# Authors: @Marthely237 & @luckyjohn-rwanda & @IreneMutamuliza
# Code to Measure time taken by program to execute.
# Importing the required module
# Question 1
import time

# store starting time
begin = time.time()

# Starting the program

for i in range(10):
    print("Welcome to DSA")

# Ending the program

time.sleep(0.5)
# store end time
end = time.time()

# total time taken
print(f"Total runtime of the program is {end - begin}")