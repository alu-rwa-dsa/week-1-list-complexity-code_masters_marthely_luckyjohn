# Authors: @Marthely237 & @luckyjohn-rwanda & @IreneMutamuliza


from matplotlib import pyplot
from time import perf_counter
import random
import re

# Question 3.1
# Find the maximum value in a list
def max_val(arr):
    return max(arr)

# list of numbers
list = [4, 32, 254, 45, 110]

# sorting the list
list.sort()

# printing the maximum value
print("The maximum value is:", list[-1])


# Question 3.2
# transform letters of a string to lower case
def lower_case(word):
    return " ".join(re.findall(r"[a-zA-Z0-9]+", word))

#Question 3.3
# Sort a list of integers
def sort_arr(arr):
    return arr.sort()

# List of Integers
numbers = [12, 5, 22, 2, 45, 36, 19]

# Sorting list of Integers
numbers.sort()

# Printing the numbers
print('the sorted list is:', numbers)


# Question 4 & 5
def plotTime(f, minArg, maxArg):
    """
    Run timer and plot time complexity
    """
    len_input = []
    t = []
    for i in range(minArg, maxArg):
        if f == lower_case:
            # string of capital As of length i
            l_input = "Marthely" + " "*i + "LuckyJohn" + " "*i
        else:
            # randomize an array of length i with values from 0 to 100
            l_input = random.sample(range(100), i)
        # Starting point
        start = perf_counter()
        # Calling the function
        f(l_input)
        #Ending point
        end = perf_counter()
        # Time to run
        len_input.append(i)
        t.append((end - start) / 1000)
    return len_input, t


def million (f):
    """
    estimating the time if the input length is 1,000,000
    """
    if f == lower_case:
        l_input = "A" * 1000000
    else:
        l_input = random.sample(range(1000000), 1000000)
    start = perf_counter()
    f(l_input)
    end = perf_counter()
    return end - start


def main():
    #  plotting the time
    print('Loading...')
    # calling the plotTime function
    len_input, t = plotTime(sort_arr, 1, 100)
    # Output
    pyplot.plot(len_input, t, 'o')
    # Graph title
    pyplot.title("Time Complexity of the Sorted list")
    # x axis
    pyplot.xlabel("List length")
    # y axis
    pyplot.ylabel("Time in (ms)")
    pyplot.show()

    len_input, t = plotTime(max_val, 1, 100)
    pyplot.plot(len_input, t, 'o')
    pyplot.title("Time Complexity of MaxValue")
    pyplot.xlabel("List length")
    pyplot.ylabel("Time ")
    pyplot.show()

    len_input, t = plotTime(lower_case, 1, 100)
    pyplot.plot(len_input, t, 'o')
    pyplot.title("Time Complexity of Lowercase ")
    pyplot.xlabel("List length")
    pyplot.ylabel("Time ")
    pyplot.show()

    # estimating the time it will take to execute input of length million
    print("Time to sort a list of integers of length one million= {} sec".format(million(sort_arr)))
    print("Time to find the max value in a list of length one million= {} sec".format(million(max_val)))
    print("Time to make strings lowercase length one million= {} sec".format(million(lower_case)))


if __name__ == '__main__':
    main()