

if __name__=="__main__":
    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])

    print(t1 == t2)

    print(id(t1[-1]))

    t1[-1].append(99)
    print(t1)

    print(t1 == t2)
