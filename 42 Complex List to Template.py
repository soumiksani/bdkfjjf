# person_one=['moris','male','Austrelia','1988',"moris@jon.com",'01-732493256']
# person_two=['vosko','male','ukrenia','1956',"vosko@mon.com",'01-732453256']

persons=[
    ['moris','male','Austrelia','1988',"moris@jon.com",'01-732493256'],
    ['vosko','male','ukrenia','1956',"vosko@mon.com",'01-732453256'],
    ['Amni', 'Female', 'Norway','1926', "Amni@jamni.com", '01-732453256'],
    ['James', 'male', 'Bangladesh','1966', "james@jamni.com", '01-732454256'],
    ['Andew', 'male', 'India','1988', "Ander@jamni.com", '01-732453236']
        ]

# print(persons[2])
# print(persons[3])
# print(persons[-1])
# print(persons[1][0])

i=0
while i < len(persons):
    singal_person= persons[i]
    name=singal_person[0]
    gendar=singal_person[1]
    country=singal_person[2]
    Birth_year=singal_person[3]
    Email=singal_person[4]
    if gendar=='male':
        pronoun='he'
        ralative='his'
    else:
        # gender='female'
        pronoun='she'
        ralative='her'
    sentence=f'{name.title()} lives in {country.title()}.{pronoun.title()} was born in {Birth_year}.{ralative.title()} email address is {Email}'
    print(sentence)
    i = i + 1
    # print(persons
    # [i])
    # print(name)
    # print(name,gendar,Email,Birth_year,country, sep='---')
    # i = i+1
