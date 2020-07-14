# Profiling Chapter Notes

## Utilizing the python timeit module 
`
python -m timeit -n 5 -r 5 -s "import {module-name}" "{module-name}.{function-name}(1000, 300)"
`

## Simple timing utilizing the unix time command
`
/usr/bin/time -p python {module-name}.py
`

## Using the cProfile module printing to stdout
`
python -m cProfile -s cumulative {module-name}.py
`

## Using the cProfile module printing to stats file for consumption using pstats
`
python -m cProfile -o {output-file-name} {module-name}.py
`

## Using line_profiler for Line-by-Line Measurements
*Dont forget to pip install line_profiler*
Also, remember to add the @profile decorator to the function you'd like to analyze line-by-line
`
kernprof -l -v {module-name}.py
`
## Splitting the abs(x) func and the n < maxiter

It can be seen through the results below that abs(z) <2 is more expensive than n < maxiter 

`
Length of x: 1000
Total complex coordinates : 1000000
Wrote profile results to julia_decorator.py.lprof
Timer unit: 1e-06 s

Total time: 65.6104 s
File: julia_decorator.py
Function: calculate_z_serial_purepython at line 18

Line #      Hits         Time  Per Hit   % Time  Line Contents

==============================================================

    18                                           @profile
    19                                           def calculate_z_serial_purepython(maxiter, zs, cs):
    20         1       2907.0   2907.0      0.0      output = [0] * len(zs)
    21   1000001     339565.0      0.3      0.5      for i in range(len(zs)):
    22   1000000     316180.0      0.3      0.5          n = 0
    23   1000000     365804.0      0.4      0.6          z = zs[i]
    24   1000000     347425.0      0.3      0.5          c = cs[i]
    25   1000000     317187.0      0.3      0.5          while True:
    26  34219980   14654445.0      0.4     22.3              not_yet_escaped = abs(z) < 2
    27  34219980   12180838.0      0.4     18.6              iterations_left = n < maxiter
    28  34219980   11478360.0      0.3     17.5              if not_yet_escaped and iterations_left:
    29  33219980   13260616.0      0.4     20.2                  z = z * z + c
    30  33219980   11660983.0      0.4     17.8                  n += 1
    31                                                       else:
    32   1000000     331685.0      0.3      0.5                  break
    33   1000000     354427.0      0.4      0.5          output[i] = n
    34         1          0.0      0.0      0.0      return output
`

## A fractional imporvement

Since we know that n < maxiter will be false atleast 10% of the time, and it's less expensive, we can place it to the left to break the loop sooner, saving time.
This can be seen below with the results of kernprof. 

### Results of expensive calc on left

`
Length of x: 1000
Total complex coordinates : 1000000
Wrote profile results to julia_lineprofiler_slower.py.lprof
Timer unit: 1e-06 s

Total time: 42.6337 s
File: julia_lineprofiler_slower.py
Function: calculate_z_serial_purepython at line 7

 Line #      Hits         Time  Per Hit   % Time  Line Contents

==============================================================

     7                                           @profile
     8                                           def calculate_z_serial_purepython(maxiter, zs, cs):
     9         1       3046.0   3046.0      0.0      output = [0] * len(zs)
    10   1000001     337333.0      0.3      0.8      for i in range(len(zs)):
    11   1000000     316787.0      0.3      0.7          n = 0
    12   1000000     368872.0      0.4      0.9          z = zs[i]
    13   1000000     349389.0      0.3      0.8          c = cs[i]
    14  34219980   16250017.0      0.5     38.1          while abs(z) < 2 and n < maxiter:
    15  33219980   12922533.0      0.4     30.3              z = z * z + c
    16  33219980   11731733.0      0.4     27.5              n += 1
    17   1000000     353999.0      0.4      0.8          output[i] = n
    18         1          1.0      1.0      0.0      return output
`

### Results of inexpensive calc on left 

`
Length of x: 1000
Total complex coordinates : 1000000
Wrote profile results to julia_lineprofiler.py.lprof
Timer unit: 1e-06 s

Total time: 40.1865 s
File: julia_lineprofiler.py
Function: calculate_z_serial_purepython at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents

==============================================================

     7                                           @profile
     8                                           def calculate_z_serial_purepython(maxiter, zs, cs):
     9         1       3009.0   3009.0      0.0      output = [0] * len(zs)
    10   1000001     316811.0      0.3      0.8      for i in range(len(zs)):
    11   1000000     299212.0      0.3      0.7          n = 0
    12   1000000     342518.0      0.3      0.9          z = zs[i]
    13   1000000     328318.0      0.3      0.8          c = cs[i]
    14  34219980   15218994.0      0.4     37.9          while n < maxiter and abs(z) < 2:
    15  33219980   12260183.0      0.4     30.5              z = z * z + c
    16  33219980   11083886.0      0.3     27.6              n += 1
    17   1000000     333538.0      0.3      0.8          output[i] = n
    18         1          0.0      0.0      0.0      return output
`
