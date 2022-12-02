# Creator JM 12/2/22

def sumTotal(number):
    sum = 0
    for x in range(0, (number + 1)):
        sum += x
    return sum

user_number = int(input('Number: '))

number_sum = sumTotal(user_number)

print(number_sum)
