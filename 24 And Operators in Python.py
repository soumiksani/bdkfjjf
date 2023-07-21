# number=int(input("Enter your number: "))
# if number >=80:
#     if number <=100:
#         print("A+")
#     else:
#         print("Invalid number")
# elif number >=70:
#     print("A")
# else:
#     print("fail")

number = int(input("Enter your number: "))
if number >= 80 and number <= 100:
    print("A+")

elif number >= 70 and number <= 79:
    print("A")
elif number <= 69 and number >=0:
    print("fail")
else:
    print("Invalid number")

