def capture(matrix):
    capture_time = 0
    threads = []
    position_of_thread = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                          (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    in_process = []
    number = -1
    for i_n, i in enumerate(matrix):
        if i[0] == matrix[0][i_n] and i[0] == 1 and i_n != 0:
            number += 1
            name = 'thread_' + str(number)
            threads.append(name)
            exec(name+'='+str(i[i_n]))
            position_of_thread[number] = (i_n, i_n)
            in_process.append((i_n, i_n))

    while_list = []
    for i in threads:
        while_list.append(eval(i))

    while [len(in_process)] + while_list != [len(matrix)-1] + [0 for _ in while_list]:
        for nn, thread in enumerate(threads):  #
            if eval(thread) == 0:
                row, column = position_of_thread[nn]
                for i_n, i in enumerate(matrix):
                    if i_n == row:
                        m = matrix[row]
                        for n, ii in enumerate(m):  # row = i_n, column = n
                            indexnxx = n
                            check = matrix[indexnxx][i_n]
                            new_thread = (indexnxx, indexnxx)
                            if ii == 1 and check == 1 and new_thread not in in_process and new_thread != (0, 0) and eval(thread) > 0:
                                number += 1
                                name = 'thread_' + str(number)
                                threads.append(name)
                                position_of_thread[number] = new_thread
                                in_process.append(new_thread)
                                exec(name + '=' + str(matrix[indexnxx][indexnxx]))
                            elif ii == 1 and check == 1 and new_thread not in in_process and new_thread != (0, 0):
                                position_of_thread[nn] = new_thread
                                in_process.append(new_thread)
                                exec(thread+'='+str(matrix[indexnxx][indexnxx]))
        capture_time += 1
        for thread in threads:
            if eval(thread) != 0:
                exec(thread+'-='+str(1))
        del while_list[:]
        for i in threads:
            while_list.append(eval(i))
    return capture_time


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
