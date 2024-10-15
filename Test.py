def countSetBits(n):
    counter = 0

    while(n>1):
        rem = n % 2
        n = n // 2
        if rem == 1:
            counter += 1
    if n == 1:
        counter += 1
    return counter 

def countSetBitsUsingBitWiseOperator(n):
    counter = 0

    while(n>1):
        #check odd, if odd is 1 remainder is 1
        counter += n&1
        n = n >> 1
    if n == 1:
        counter += 1
    return counter


def countSetBitsUsingRemoveLastSetBit(n):
    counter = 0

    while (n>0):
        counter += 1
        n = n & n-1

    return counter


n = 15 #01111
print(countSetBitsUsingRemoveLastSetBit(n))


"""
n = 16

Iterate and check if rem is 1
check if n is 1 at last


Bit Wise Solution (use >> to divide)

1000 >> 1 = 100 (4)
100 >> 1 = 10 (2)
10 >> 1 = 01 (1)


Remove Last Set Bit (keep removing last set bit untill it becomes 0)

N = 84

    1010100
N-1 1010011
    --------
&   1010000

    1010000
    1000000
    -------
&   1000000


    1000000
    0111111
    --------
    0000000


"""