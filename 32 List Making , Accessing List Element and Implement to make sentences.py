user_one= ['abrar',26,False, "noyabari"]
# print(type(user_one))  # list
# print(len(user_one))

#           0       1       2        3
#           -4      -3      -2      -1

# print(user_one[0], user_one[-4],sep="-----")
# print(user_one[1], user_one[-3],sep="-----")
# print(user_one[2], user_one[-2],sep="-----")
# print(user_one[3], user_one[-1],sep="-----")

# partial_list=user_one[1:3]
# print(partial_list)

#john soe is a man of 26 year old who lives in kamkuk kamakkha

name=user_one[0]
age=user_one[1]
living_place=user_one[3]
is_male=user_one[2]
if is_male:
    pronoun='He'
    gender='man'
else:
    pronuon='she'
    gender='woman'
sentence=f'{name} is a {gender} of {age} year old who lives in  {living_place}'
print(sentence)