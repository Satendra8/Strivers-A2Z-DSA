def sjf(bt):
    """
    Optimal Approach
    bt = [4,3,7,1,2]
        0 1 2 3 4
    bt = [1,2,3,4,7] #sort

        1     2       3       4       7
    0------1------3-------6-------10-------17

    process  waiting time
    p0 -------> 0
    p1 -------> 1
    p2 -------> 3
    p3 -------> 6
    p4 -------> 10
    -------------------
    total       20
    -------------------
    AVG = 20/5 = 4
    """
    n = len(bt)
    bt.sort()
    waiting_time = 0
    total_time = 0

    for i in range(n-1):
        waiting_time += bt[i]
        total_time += waiting_time
    return int(total_time/n)


bt = [1,2,3,4]
print(sjf(bt))