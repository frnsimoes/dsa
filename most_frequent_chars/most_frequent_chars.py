def most_frequent_char(s):
    counter_hash = {}

    for char in s:
        if char not in counter_hash.keys():
            counter_hash[char] = 0
        counter_hash[char] += 1

    best = None
    for char in s:
        if not best:
            best = char
        if counter_hash[char] > counter_hash[best]:
            best = char
    return best



if __name__ == '__main__':
    assert most_frequent_char('mississippi') == 'i'
    assert most_frequent_char('eleventennine') == 'e'
    assert most_frequent_char('bookeeper') == 'e'
    assert most_frequent_char('riverbed') == 'r'
    assert most_frequent_char('david') == 'd'
