'''
 istitle(), isupper(), islower(), isspace(), isidentifier(), "encode"  mehod er babohar
'''
str1='Python'
str2='python'
str3='I Love Python'
str4=' '
str5='abdulAwal'
str6='7abdul'
str7='Ståle'
str8="b'St\xc3\xa5le'"
# print(str1.istitle())
# print(str2.istitle())
# print(str2.islower())
# print(str4.isspace())
print(str5.isidentifier())
print(str5.isidentifier(),str6.isidentifier())


print("normal print:",str7)
print("encoded print:",str7.encode())
