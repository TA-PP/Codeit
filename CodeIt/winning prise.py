i = 50000000
year = 1988
j = 1100000000

while(year <= 2015):
     i *= 1.12
     year+=1 
    
if(i > j):
    print("{:.0f}원 차이로 동일 아저씨 말씀이 맞습니다.".format(i - j))
elif(i < j):
    print("{:.0f}원 차이로 미란 아주머니 말씀이 맞습니다.".format(j - i))
