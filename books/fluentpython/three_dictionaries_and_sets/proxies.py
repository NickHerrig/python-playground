def main():
    from types import MappingProxyType
    d = { 1: 'A' }
    d_proxy = MappingProxyType(d)
    return d_proxy



if __name__=="__main__":
    immutable = main()
    print(immutable[1])
    immutable[2] = "this should fail"
