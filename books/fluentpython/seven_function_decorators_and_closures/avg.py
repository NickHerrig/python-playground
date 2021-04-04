#object oriented implementation
class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


#function implementation

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

# more efficient impl with nonlocal

def make_eff_averager():
    count = 0
    total = 0

    def eff_averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count

    return eff_averager

def main():
    avg = Averager()
    print(avg(5))
    print(avg(5))
    print(avg(6))

    avg = make_averager()
    print(avg(5))
    print(avg(5))
    print(avg(6))

    avg = make_eff_averager()
    print(avg(5))
    print(avg(5))
    print(avg(6))


if __name__=="__main__":
    main()

