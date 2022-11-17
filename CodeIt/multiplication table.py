first = 1
second = 1

while(second <= 9):
    print("{} * {} = {}".format(first, second, first * second))
    second+=1
    while(second == 10 and first < 9):
        first+=1
        second = 1
