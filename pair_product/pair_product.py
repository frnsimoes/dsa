def pair_product(numbers, target_product):
    prev_numbers = {}
    for i, n in enumerate(numbers):
        complement = target_product / n

        if complement in prev_numbers:
            return i, prev_numbers[complement]

        prev_numbers[n] = i
