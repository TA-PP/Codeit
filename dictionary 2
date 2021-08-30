with open('vocabulary.txt', 'r',encoding = 'UTf - 8') as f:
       for word in f:
                voca = word.split()
                new_voca = voca[0].split(":")
                final_voca = new_voca[0]
                kor_word = voca[1]
                ans = input('{}: '.format(kor_word))

                if(ans == final_voca):
                       print('맞았습니다!\n')
                else:
                        print('아쉽습니다. 정답은 {}입니다.\n'.format(final_voca))
