import random
person=('moris','chittagong')
name=person[0]
location=person[1]

sentence_one_group=[
    f'this is {name.title()}',
    f'My name is {name.title()}',
    f'{name} is my name'
]
sentence_two_group=[
    f'I live live in {location} ',
    f'I reside in {location}',
    f'I was raised in {location}',
    f'{location} is the place were i reside '
]
sentence_one =random.choice(sentence_one_group)
sentence_two =random.choice(sentence_two_group)

paragraph=f'{sentence_one}.{sentence_two}'
print(paragraph)
# print(sentence_one)
# print(sentence_two)