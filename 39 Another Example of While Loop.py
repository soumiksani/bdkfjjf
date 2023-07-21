Years=[1988,3214,2020,2022,1956,1578]

i=0

while i < len(Years):
    if Years[i] % 4 == 0:
        print(Years[i],"is leap year")
    i= i + 1