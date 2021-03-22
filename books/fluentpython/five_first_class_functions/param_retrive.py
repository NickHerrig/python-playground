
def woah(name, num_woah=1):
    return "woah " * num_woah + name

def woah_two(name, num_woah=1) -> str:
    return "woah " * num_woah + name

def main():
    print(woah("nick"))
    print(woah("nick", 5))

    # An awkward way of function introspection.
    print(woah.__defaults__)
    print(woah.__code__.co_varnames)
    print(woah.__code__.co_argcount)

    # A better way...
    from inspect import signature
    sig = signature(woah)
    print(sig)
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

    import inspect

    # inspecting the function annotation
    print(woah_two.__annotations__)
    sig = inspect.signature(woah_two)
    print(sig.return_annotation)

    sig = inspect.signature(woah)
    my_woah = {'name': 'nick', 'num_woah': 6}
    bound_args = sig.bind(**my_woah)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)

    # validating defaults
    my_woah = {'num_woah': 6}
    bound_args = sig.bind(**my_woah)



if __name__=="__main__":
    main()

