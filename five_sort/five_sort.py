def five_sort(nums):
    i = 0
    j = len(nums) -1

    while j > i:
        i_is_five = nums[i] == 5
        j_is_five = nums[j] == 5

        if not i_is_five:
            i += 1

        if j_is_five:
            j -= 1


        if i_is_five and not j_is_five:
            nums[i], nums[j] = nums[j], nums[i]
    print(nums)
    return nums


assert five_sort([12, 5, 1, 5, 12, 7]) == [12, 7, 1, 12, 5, 5]
assert five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]) == [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]
