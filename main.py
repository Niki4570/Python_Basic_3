def reverse_number(num, reversed_num = 0):
    while num != 0:
        remain = num % 10
        reversed_num = (reversed_num * 10) + remain
        num = num // 10
    return reversed_num


num = int(input("Enter your number: "))
reversed_num = reverse_number(num)
print("Reversed number:", reversed_num)
