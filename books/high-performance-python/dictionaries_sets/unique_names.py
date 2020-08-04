def unique_names_sets(phonebook):

    unique_names = set()

    for name, phone in phonebook:
        first_name, last_name = name.split(" ", 1)
        unique_names.add(first_name)

    return len(unique_names)

def unique_names_lists(phonebook):

    unique_names = []
    for name, phonenumber in phonebook:
        first_name, last_name = name.split(" ", 1)
        for unique in unique_names:
            if unique == first_name:
                break
        else:
            unique_names.append(first_name)
    return len(unique_names)


def main():
    phonebook = [
        ("Nick Herrig", "111-111-1111"),
        ("Megan Komos", "222-222-2222"),
        ("Nick Bloopy", "411-511-1111"),
        ("Megan Jeffries", "222-922-2122"),
        ("Billy Bob", "992-922-2122"),
        ("Phil Billy", "201-922-2122"),
    ]

    print("sets func: ", unique_names_sets(phonebook))
    print("lists func: ", unique_names_lists(phonebook))

if __name__=="__main__":
    main()
