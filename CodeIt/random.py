import random

# 코드를 작성하세요.
answer = random.randint(1, 20)

for i in range(1,5):
    approach = int(input('기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: '.format(5 - i)))
    if(approach < answer):
        print('Up')
    elif(approach > answer):
        print('Down')
    else:
        print('축하합니다. {}번만에 숫자를 맞히셨습니다.'.format(i))
        break
            
if(i == 4 and approach != answer):  
    print('아쉽습니다. 정답은 {}였습니다.'.format(answer))
