from wp_func import wp_p
from wp_func import wp_h2


first_paragraph_text = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."

heading_one_text = "Why do we use it?"
second_paragraph_text = "It is a long established fact that a reader will be distracted by the readable content"

article = wp_p(first_paragraph_text)+wp_h2(heading_one_text)+wp_p(second_paragraph_text)

print(article)

#
#
# # Python code to demonstrate the working of
# # calendar() function to print calendar
#
# # importing calendar module
# # for calendar operations
# import calendar
#
# # using calendar to print calendar of year
# # prints calendar of 2018
# print("The calendar of year 2018 is : ")
# print(calendar.calendar(2023))