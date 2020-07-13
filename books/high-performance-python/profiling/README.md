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
