stop = '100500'
yes_no = False

while True:
    numbers = input().split('; ')
    if stop in numbers:
        break

    numbers = [int(num) for num in numbers]
    first_number = numbers.pop(0)
    answ = sorted(num for num in numbers if num % first_number == 0)

    if yes_no:
        max_min_number = min(answ)
    else:
        max_min_number = max(answ)

    print(' '.join(str(num) for num in answ), max_min_number)

    yes_no = not yes_no
