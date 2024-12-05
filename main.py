print("Дано число n в восьмеричной системе счисления ,состоящее из 5 чисел.Выведите на экран значение этого числа в десятичной системе счисления")
n = int(input("Введите число из пяти цифр: "))
eight_last = n % 10
n //= 10
ten_last = eight_last * (8**0)
eight_prev = n % 10
n //= 10
ten_prev = eight_prev * (8**1)
eight_third = n % 10
n //= 10
ten_third = eight_third * (8**2)
eight_second = n % 10
n //= 10
ten_second = eight_second * (8**3)
eight_first = n % 10
n //= 10
ten_first = eight_first * (8**4)
sum = ten_last + ten_prev + ten_third + ten_second + ten_first
print(f"число{n} в восьмеричной СС равняется числу {sum} в десятичной СС")