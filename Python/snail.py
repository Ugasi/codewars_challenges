def snail(array):
    horizontal = 0
    vertical = 0
    max_h = len(array[0])-1
    max_v = len(array)-1
    total = len(array)*len(array[0])
    min_h = 0
    min_v = 0
    result_array = []
    while len(result_array) != total:
        for i in range(min_h, max_h+1):
            horizontal = i
            result_array.append(array[vertical][horizontal])
            print(array[vertical][horizontal])
        min_v += 1
        for i in range(min_h+1, max_v+1):
            vertical = i
            result_array.append(array[vertical][horizontal])
            print(array[vertical][horizontal])
        max_h -= 1
        for i in range(max_h, min_h-1, -1):
            horizontal = i
            result_array.append(array[vertical][horizontal])
            print(array[vertical][horizontal])
        max_v -= 1
        for i in range(max_v, min_v-1, -1):
            vertical = i
            result_array.append(array[vertical][horizontal])
            print(array[vertical][horizontal])
        min_h += 1
    return result_array
    # for i in range(len(array)*len(array[0])):
    #     if horizontal == 0 and vertical == 0:
    #         horizontal += 1
    #     elif horizontal < max_h and horizontal >= vertical:
    #         horizontal += 1
    #     elif vertical < horizontal:
    #         vertical += 1
    #     elif vertical == max_v and horizontal != min_h:
    #         horizontal -= 1
    #     elif horizontal == min_h and vertical > horizontal+1:
    #         vertical -= 1
    #     elif vertical == horizontal+1:
    #         horizontal += 1

#0 0, 0 1, 0 2, 0 3, 1 3, 2 3, 3 3, 3 2, 3 1, 3 0, 2 0, 1 0, 1 1, 1 2, 2 2, 2 1
#0 0, 0 1, 0 2, 1 2, 2 2, 2 1, 2 0, 1 0, 1 1

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array)
