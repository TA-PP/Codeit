def calculate_change(payment, cost):
    # 코드를 작성하세요.
    change = payment - cost
    print("50000원 지폐: {}장".format(change // 50000))
    change_1 = change // 50000
    print("10000원 지폐: {}장".format((change - (change_1 * 50000)) // 10000))
    change_2 = (change - (change_1 * 50000)) // 10000
    print("5000원 지폐: {}장".format((change - (change_1 * 50000 + change_2 * 10000)) // 5000))
    change_3 = (change - (change_1 * 50000 + change_2 * 10000)) // 5000
    print("1000원 지폐: {}장".format((change -(change_1 * 50000 + change_2 * 10000 + change_3 * 5000)) // 1000))
# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
