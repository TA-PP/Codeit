from random import randint

def generate_numbers(n):
    num_list = []

    for i in range(1, n + 1):
        number = randint(1, 45)
        if(number not in num_list):
            num_list.append(number)
        else:
            number = randint(1, 45)
            num_list.append(number)
         
    return num_list

def draw_winning_numbers():
    new_list = generate_numbers(6)
    for i in range(len(new_list) - 1):
        temp = i

        for j in range(i + 1, len(new_list)):
            if(new_list[j] < new_list[temp]):
                temp = j
                
        new_list[i], new_list[temp] = new_list[temp], new_list[i]

    number = randint(1, 45)
    if(number not in new_list):
        new_list.append(number)
    else:
        number = randint(1, 45)
        new_list.append(number)  

    return new_list

def count_matching_numbers(numbers, winning_numbers):
  
    count = 0
    for num1 in range(len(numbers)):
        for num2 in range(len(winning_numbers)):
            if(numbers[num1] == winning_numbers[num2]):
                count += 1

    return count

def check(numbers, winning_numbers):
    total = count_matching_numbers(numbers, winning_numbers[:6])
    final = count_matching_numbers(numbers, winning_numbers[6:])

    if(total == 6):
       return 1000000000
    elif(total == 5 and final == 1):
        return 50000000
    elif(total == 5):
        return 10000000
    elif(total == 4):
        return 50000
    elif(total == 3):
        return 5000
    else:
        return 0


print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
