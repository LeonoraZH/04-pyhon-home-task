# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите натуральное число: '))


def fill_nutural_numbers(n: int):
    natural_numbers = []
    for i in range(2, int(n / 2)):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            natural_numbers.append(i)
    return natural_numbers


natural_numbers = fill_nutural_numbers(number)
print(natural_numbers)


def find_prime_factors(numbers: list, n: int):
    prime_factors = []
    for i in numbers:
        if n % i == 0:
            prime_factors.append(i)
            n /= i
    return prime_factors


print(find_prime_factors(natural_numbers, number))
