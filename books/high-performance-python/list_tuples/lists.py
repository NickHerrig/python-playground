from functools import wraps
import time

large_list = [x for x in range(100000)]
small_list = [x for x in range(10)]

def time_function(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print("@time_function: ", fn.__name__, "took ", total_time, " seconds.")
        return result
    return measure_time

@time_function
def linear_search(my_array, my_needle):
    for index, value in enumerate(my_array):
        if value == my_needle:
            return index

@time_function
def binary_search(haystack, needle):
    minimum, maximum = 0, len(haystack)

    while True:
        if minimum >= maximum:
            return -1
        middle = (minimum + maximum) // 2

        if haystack[middle] > needle:
            maximum = middle
        elif haystack[middle] < needle:
            minimum = middle + 1
        else:
            return middle


def fetch_needle(my_arry, needle_index):
    return my_list[my_index]


def main():

    print(binary_search(large_list, 88))
    print(binary_search(large_list, 1))

if __name__=="__main__":
    main()

