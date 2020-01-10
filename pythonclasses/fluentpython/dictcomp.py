DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]


my_dict = { country: code for code, country in DIAL_CODES}
print(my_dict)

my_new_dict = { country: code for code, country in DIAL_CODES if code < 82}
print(my_new_dict)
