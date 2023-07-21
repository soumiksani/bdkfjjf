# normal_body_temp= 98.6
# temp=float(input("Enter your temperature: "))
# if temp > normal_body_temp:
#     print("paracitamol 2 bela ")
# else:
#     print('vitamin tablet 3 bela')
#

#jalanta is an actor of Bangladesh. He is nayok
#rain is an actress of Bangladesh. she is nayika

name= input('enter name: ')
gender= input("Enter gender (m/f): ")
country=input("Enter country: ")
# profession, pronoun, known_as

if gender == 'm':
    profession='actor'
    pronoun='he'
    known_as= 'nayok'
else:
    profession='actress'
    pronoun= "She"
    known_as="nayika"

print(f"{name} is an {profession} of {country}. He is {known_as}")
