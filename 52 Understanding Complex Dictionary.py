user_1 ={
    'username':'jalanto',
    "password":'rain',
    'role':'admin'
}

user_2={'username':'shakib khan',
    "password":'googlyapu',
    'role':'constributor'
}

users=[{
    'username':'jalanto',
    "password":'rain',
    'role':'admin'
},
{'username':'shakib khan',
    "password":'googlyapu',
    'role':'constributor'
}]
for user in users:
    print(user.get("username"))
    print(user.get("role"))