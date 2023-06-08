dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (1, 'Canada'),
    (86, 'China'),
    (49, 'Germany'),
    (91, 'India'),
    (39, 'Italy'),
    (81, 'Japan'),
    (7, 'Russia'),
    (44, 'United Kingdom'),
    (1, 'United States'),
]

county_dial = {country: code for code, country in dial_codes}
new_county_dial = {code: country.upper()
        for country, code in sorted(county_dial.items())
        if code < 70}

print(county_dial)
print(new_county_dial)
