from random import randint

def generate_numbers():
    numbers = []
    
    for i in range(3):
        random_number = randint(0,9)

        if(random_number not in numbers):
            numbers.append(random_number)
        else:
            random_number = randint(0,9)
            numbers.append(random_number)
    
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    # 코드를 작성하세요.
    for i in range(3):
        guess = int(input('{}번째 숫자를 입력하세요: '.format(i + 1)))

        if(guess in new_guess):
            print('중복되는 숫자입니다. 다시 입력하세요.')
            guess_1 = int(input('{}번째 숫자를 입력하세요: '.format(i + 1)))
            new_guess.append(guess_1)
        elif(guess not in range(10)):
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
            guess_2 = int(input('{}번째 숫자를 입력하세요: '.format(i + 1)))
            new_guess.append(guess_2)
        else:
            new_guess.append(guess)

    return new_guess

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(3):

            if(guess[i] in solution and guess[i] != solution[i]):
                ball_count += 1
            elif(guess[i] == solution[i]):
                strike_count += 1
            
    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 코드를 작성하세요.
while True:
    guess = take_guess()
    score = get_score(guess, ANSWER)
    print('{}S {}B'.format(score[0], score[1]))
    tries += 1

    if(score == (3,0)):
        break


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
