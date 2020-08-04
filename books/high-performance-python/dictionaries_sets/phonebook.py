def lookup_phone(phonebook, name):
    for n, p in phonebook:
        if n == name:
            return p
    return None

#O(n) lookup speed for linear search over a list
def main():
    phonebook_list = [
        ("Nick", "111-111-1111"),
        ("Megan", "222-222-2222"),
    ]

    print("Nicks phone number is ", lookup_phone(phonebook_list, "Nick"))

if __name__=="__main__":
    main()
