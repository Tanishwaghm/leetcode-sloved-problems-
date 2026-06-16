def remove_duplicates(lst):
    result = []

    for num in lst:
        found = False   # assume not found

        for x in result:
            if x == num:
                found = True   # duplicate found
                break

        if not found:   # only add if NOT found
            result.append(num)

    return result
