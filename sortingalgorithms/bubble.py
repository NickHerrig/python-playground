def bubblesort(list):
    listlength= len(list)
    for i in range(listlength):
        for j in range(0 , listlength - i - 1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list
