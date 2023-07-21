def add(a,b):
    """
    return total of two number
    """
    total = a+b
    return total
#
# print(add(3,5))

def multiple_add(*args):
    total = 0
    for number in args:
        total += number
    return total
result = multiple_add(2,3,4,55.6,6.67)
print(result)