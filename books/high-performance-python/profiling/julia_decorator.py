import time
from functools import wraps

# If using timit, run the following command:
# python -m timeit -n 5 -r 5 -s "import julia_decorator" "julia_decorator.calc_pure_python(1000, 300)"

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

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
def calculate_z_serial_purepython(maxiter, zs, cs):
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output


def calc_pure_python(desired_width, max_iterations):
    """
    Creates a list of complex coordinates and complex parameters
    """

    x_step = (float(x2 - x1) / float(desired_width))
    y_step = (float(y1 - y2) / float(desired_width))
    x = []
    y = []

    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step

    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    complex_coordinates = []
    complex_parameters = []

    for ycoord in y:
        for xcoord in x:
            complex_coordinates.append(complex(xcoord, ycoord))
            complex_parameters.append(complex(c_real, c_imag))

    print("Length of x:", len(x))
    print("Total complex coordinates :", len(complex_coordinates))

    output = calculate_z_serial_purepython(max_iterations, complex_coordinates, complex_parameters)

    assert sum(output) == 33219980

if __name__ == "__main__":
    calc_pure_python(desired_width=1000, max_iterations=300)
