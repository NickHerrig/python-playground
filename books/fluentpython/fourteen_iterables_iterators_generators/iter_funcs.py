import itertools
import operator

def vowel(c):
    return c.lower() in 'aeiou'

def main():
    print(list(filter(vowel, 'Aardvark')))
    print(list(itertools.filterfalse(vowel, 'Aardvark')))
    print(list(itertools.dropwhile(vowel, 'Aardvark')))
    print(list(itertools.takewhile(vowel, 'Aardvark')))
    print(list(itertools.compress('Aardvark', (1,0,0,0,0,1,1))))
    print(list(itertools.islice('Aardvark', 5)))

    sample = [ 5, 4, 2, 8, 7, 6, 3, 0, 9, 1 ]
    print(list(itertools.accumulate(sample)))
    print(list(itertools.accumulate(sample, min)))
    print(list(itertools.accumulate(sample, max)))
    print(list(itertools.accumulate(sample, operator.mul)))
    print(list(itertools.accumulate(range(1, 11), operator.mul)))



if __name__=="__main__":
    main()
