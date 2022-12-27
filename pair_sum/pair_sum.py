def pair_sum(numbers, target_sum):
    pairs = {}
    for i, n in enumerate(numbers):
        target = target_sum - n
        if target in pairs:
            return i, pairs[target]

        pairs[n] = i
