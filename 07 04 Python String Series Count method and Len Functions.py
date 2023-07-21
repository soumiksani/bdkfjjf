# "count" len useage
str1="python is awsome.isn't is."

#Count the length

print("the total character is:",len(str1))

#count method
subtring="is"
subtring1="awsome"
print(str1.count("is"))
print("The substring",subtring1,"present",str1.count(subtring1),"times")
print("The substring",subtring,"present",str1.count(subtring),"times")

subtring3='i'
print(str1.count(subtring3,8,20))

#string.count(subtring ------- Return total count
#string.count(subtring,start, end) ------- Return total count between stat