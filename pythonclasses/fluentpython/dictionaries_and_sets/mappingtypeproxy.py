from types import MappingProxyType

data = {1: 'A'}
data_proxy = MappingProxyType(data)
print(data_proxy)
print(data_proxy[1])

try:
    print(data_proxy[2])
except Exception:
    print("2 doesn't exist yet..")
    pass

data[2] = 'B'
print(data_proxy[2])
