with open('vocabulary.txt', 'a') as f:
        while True:
                eng_word = input('영어 단어를 입력하세요: ')
                kor_word = input('한국어 뜻을 입력하세요: ')

                f.write('{}: {}\n'.format(eng_word, kor_word))

                if( input('영어 단어를 입력하세요: ') == 'q'):
                        break
