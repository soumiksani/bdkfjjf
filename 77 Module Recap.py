def f2c(temp):
    # celcious = round((temp-32)*5/9,2)
    celcious = round((temp-32)*5/9,5)
    return celcious
print(f2c(96))