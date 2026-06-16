def check_unique(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False   # duplicate found
    return True   # no duplicates
