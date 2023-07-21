post={
    'id':100,
    "title":'This is awesome titles',
    "content":'This are awesome contents',
    'author':'Awesome name',
    "catagories":'awesome',
    "slug":'awesome title'
}

# post["catagories"]='genius' #updating data
# post.update({"catagories":'genius'})
# post.update({'sticky': True})
# post['sticky']= True
# print(post)

car={
    'name':'Toyota',
    'year':2000
}
car['year']= 2002
print(car)
car.update({'colour':'yellow'})
print(car)
print(car.get('colour'))
print(car['name'])