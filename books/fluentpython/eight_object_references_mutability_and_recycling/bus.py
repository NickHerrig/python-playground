import copy


class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class HauntedBus:
    """This is no bueno! do not use mutable types as param defaults"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def main():
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 =  copy.copy(bus1)
    bus3 =  copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))
    bus1.drop('Bill')
    print(bus2.passengers)
    print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
    print(bus3.passengers)

    bus_nick = HauntedBus()
    bus_nick.pick('Alice')
    print(bus_nick.passengers)

    """The problem is that HauntedBus instances that
       don’t get an initial passenger list end
       up sharing the same passenger list among themselves."""

    bus_bug = HauntedBus()
    print(bus_bug.passengers)
    print(bus_bug.passengers is bus_nick.passengers)


if __name__=="__main__":
    main()
