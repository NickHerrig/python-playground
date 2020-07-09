# Profiling Chapter Notes

## Utilizing the python timeit module 
`
python -m timeit -n 5 -r 5 -s "import julia_decorator" "julia_decorator.calc_pure_python(1000, 300)"
`

## Simple timing utilizing the unix time command
`
/usr/bin/time -p python {script-name}.py
`
