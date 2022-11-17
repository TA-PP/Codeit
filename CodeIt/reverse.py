numbers = [2, 3, 5, 7, 11, 13, 17, 19]
 
                
for i in range(0, len(numbers)-1):
        big = numbers[i]
        temp = i
        for j in range(i+1, len(numbers)):
                if(numbers[j] > big):
                        temp = j
                        big = numbers[j]
        
        numTemp = numbers[i]
        numbers[i] = big
        numbers[temp] = numTemp
        

print("뒤집어진 리스트: " + str(numbers))
