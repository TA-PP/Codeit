# 자리수 합 리턴
def sum_digit(num):
        # 코드를 입력하세요.
        total = 0
        i = 0
        num = str(num)
        
        if(len(num) == 1):
                total = int(num)
                return total
        elif(len(num) == 2):
                first = num[i]
                second = num[i+1]
                total = int(first) + int(second)
                return total 
        elif(len(num) == 3): 
                first = num[i]
                second = num[i+1]
                third = num[i+2]
                total = int(first) + int(second) + int(third)
                return total
        else:
                total = 1 
                return total
        

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
counter = 0
for i in range(1, 1001):
       counter += sum_digit(i)

print(counter)
