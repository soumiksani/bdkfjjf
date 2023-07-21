user={
    'id':'1',
    "first name":'soumik',
    'last name':'sani',
    'username':'admin',
    'password':'123456789',
    "role":'admin'
}
# first_name=user['first name']
# last_name=user['last name']
# print(first_name,last_name )
#
# first_name=user.get('first name')
# last_name=user.get('last name')
# print(first_name,last_name)

keys=user.keys()
values=user.values()
print(list(keys))
print(list(values))
