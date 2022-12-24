def anagrams(s1, s2):
    if not len(s1) == len(s2):
        return False

    return count_chars(s1) == count_chars(s2)

def count_chars(s):
    count = {}
    for c in s:
        if count.get(c):
            count[c] += 1
            continue
        count[c] = 1
    return count


if __name__ == '__main__':
    assert anagrams('elbow', 'below')
    assert anagrams('paper', 'reapa') is False


"""
123456
restful

"""
