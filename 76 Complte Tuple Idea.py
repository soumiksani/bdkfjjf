def area_volume(lenght,width,hight):
    """
    return area and volume of any object
    """
    area = lenght*width
    volume = lenght*width*hight
    return area,volume,lenght,width
test = area_volume(3,4,5)
# print(type(test))
print(test)
print(test[1])
test_list=list(test)
test_list[0]=9
test_tup=tuple(test_list)
print(test_tup)