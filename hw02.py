def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 that are divisible by 7
    >>> c
    0
    """
    count = 0
    num = 1
    while num <= n:
        if num % k == 0:
            count += 1
            print(num)
        num += 1
    return count



def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    count = 0
    while n!=1:
        print(n)
        count+=1
        if n % 2 == 0:
            n = n//2
        elif n % 2 == 1:
            n = (3*n)+1
    print(n)
    count+=1
    return count