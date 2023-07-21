car={
    "brand":'ford',
    'model':'mustang',
    'year':2010,
    'colour':'black',
}

# print(car.get("brand"))
# car.update({'colour':"blue"})
print(car)
car.pop('colour')
car.pop('year')
print(car)
