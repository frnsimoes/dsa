def uncompress(s):
    result = []
    i = 0
    j = 0

    while j < len(s):
        character = s[j]
        if character.isnumeric():
            j += 1  # targets the numeric value index
        else:
            found_number = int(s[i:j])
            result.append(found_number * character)
            j += 1
            i = j

    return ''.join([x for x in result])


if __name__ == '__main__':
    assert uncompress('2b3c') == 'bbccc'
