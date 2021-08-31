def binary_search(element, some_list):
    # 코드를 작성하세요.
    for i in range(len(some_list)):
        j = (0 + (len(some_list) - 1)) // 2
        
        if(element == some_list[j]):
            return j
        elif(element <= some_list[j]):
            some_list_1 = some_list[0:j]
            for k in range(len(some_list_1)):
                l = (0 + (len(some_list_1) - 1)) // 2
                if(element == some_list[l]):
                    return l
                elif(element >= some_list[l]):
                    return l+1
        elif(element >= some_list[j]):
            some_list_2 = some_list[j:]
            for k in range(len(some_list_2)):
                l = (j + (len(some_list) - 1)) // 2
                if(element == some_list[l]):
                    return l
                elif(element >= some_list[l]):
                    return l+1

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
