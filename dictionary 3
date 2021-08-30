import random

voca = {}

with open('vocabulary.txt', 'r') as f:
        for line in f:
                data = line.strip().split(': ')
                eng_word, kor_word = data[0], data[1]
                voca[eng_word] = kor_word

while True:
        keys = list(voca.keys())
        index = random.randint(0, len(keys) - 1)
        eng_word =  keys[index]
        kor_word = voca[eng_word]
        ans = input('{}: '.format(kor_word))

        if(ans == eng_word):
                print('맞았습니다!\n')
        elif(ans == 'q'):
                break
        else:
                print('아쉽습니다 정답은 {}입니다.\n'.format(eng_word))
