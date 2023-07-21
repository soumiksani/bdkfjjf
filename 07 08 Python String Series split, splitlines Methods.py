# spilt,rsplit,issplit,slitline  er babohar

str1="hello, my name is soumik,\n I am 20 years old."

print(str1.split())   # space
print(str1.split(","))   # comma
print(str1.split(",", maxsplit=1))   # max split

# print(str1)
print(str1.splitlines())
print(str1.splitlines(True))
print(str1.splitlines(False))
print(str1.splitlines())
