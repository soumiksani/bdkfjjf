# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years and salary greater than 20000 usd.
#Ask user for thier salary and year of service and print the net bonus amount.

salary=int(input("Enter your salary:"))
years_of_service= int(input("Enter your year of service:"))

# if years_of_service > 5 and salary >= 20000:
#     bonus=0.05
#     net_salary=salary + salary * bonus
#     print("Your net salary with bonus",net_salary, 'USD')
#
# else:
#     print("you get only your salary",salary, 'USD')


if years_of_service > 5 or salary >= 20000:
    bonus=0.05
    net_salary=salary + salary * bonus
    print("Your net salary with bonus",net_salary, 'USD')

else:
    print("you get only your salary",salary, 'USD')