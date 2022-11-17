i = 120
n=1
number=0

while n<=120:
    if(i % n == 0):
        print(n)
        number+=1
    n+=1

print("120의 약수는 총 {}개입니다.".format(number))
