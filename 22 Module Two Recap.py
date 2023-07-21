#he is going to cox's bazar
# print("he is going\n\t to cox\'s bazar")
#
# print("Aouwal" != "aouwal")
# #comparison oparator : < , > , <= , >= , !=

# gender=(input("enter gender m/f: "))
# if gender == "m":
#     pronoun= "he"
#     profession="Actor"
#     ralative="him"
# else:
#     pronoun ="She"
#     profession ="actress"
#     ralative="her"
#
# print(f"{pronoun} is an {profession}.i know {ralative}")
#
# number = 5
# guess=int(input("enter your number: "))

# if guess == number:
#     print("Yah, you have guessed right number")
# elif guess > number:
#     print("you have entered larger number")
# # #elif guess < number:
# #  #   print("YOU have entered smaller number ")
# else:
#     print("you have entered smaller number")
number = 5
guess=int(input("enter your number: "))

if guess != number:
    if guess > number:
        print(" you have Entered number larger number")
    else:
        print("you have Entered number smaller number")
else:
    print("You have won the game")
