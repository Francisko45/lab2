
def count_positive_numbers(numbers):
    return sum(1 for num in numbers if num > 0)


numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

positive_count = count_positive_numbers(numbers)
print("Кількість додатних чисел:", positive_count)
