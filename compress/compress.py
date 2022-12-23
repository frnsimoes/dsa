def compress(s):
    j = 0
    i = 0
    result = ""

    while j < len(s):
        if s[j] == s[i]:
            j += 1

        else:
            letter = s[i]
            num = len(s[i:j])
            result += f"{num}{letter}"

            i = j

    return result




if __name__ == '__main__':
    result = compress('bbbcccc')
    expected = '3b4ct'
    assert result == expected
