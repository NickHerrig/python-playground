import weakref

def main():
    print("The object is garbage collected")


if __name__=="__main__":
    s1 = {1, 2, 3, 5}
    s2 = s1
    ender = weakref.finalize(s1, main)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 'spam'
    print(ender.alive)
    print(s2)
