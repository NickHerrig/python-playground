def main():
    dial_codes = [
            (86, "China"),
            (91, "India"),
            (1, "United States"),
            (62, "Indonesia"),
        ]

    country_code = { country: code for code, country in dial_codes }
    from pprint import pprint
    pprint(country_code)

    country_code = { code: country.upper() for code, country in dial_codes
                     if code < 70 }
    pprint(country_code)


if __name__=="__main__":
    main()

