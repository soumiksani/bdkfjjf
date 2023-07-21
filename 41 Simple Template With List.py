person_one=['moris',
            'male',
            'Austrelia',
            '29 january 1988',
            "moris@jon.com",
            '01-732493256']

person_two=['vosko',
            'male',
            'ukrenia',
            '29 octber 1956',
            "vosko@mon.com",
            '01-732453256']






gender_one=person_one[1]
if gender_one=="male":
    relative='his'
    pronoun='he'
else:
    relative="her"
    pronoun='she'


sentence=f"{person_one[0].title()} is born {person_one[2].title()}.{relative.title()} date of birth is {person_one[3].title()}.{pronoun.title()} is available at {person_one[4].title()} and phone no number is {person_one[-1]}"
print(sentence)

#title make the letter upper hand