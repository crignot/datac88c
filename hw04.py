def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    >>> home = intersection(10, 10)
    >>> work = intersection(14, 13)
    >>> taxicab(home, work)
    7
    >>> taxicab(work, home)
    7
    """
    return abs(street(a)-street(b)) + abs(avenue(a)-avenue(b))


def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b)  # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a  # a's prefix [1,1,3,2] is replaced with b's prefix [4,3]
    [4, 3, 1, 1, 4]
    >>> b  # b's prefix [4,3] is replaced with a's prefix [1,1,3,2]
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)  # No prefixes with equal sum
    'No deal!'
    >>> b  # b remains unchanged
    [1, 1, 3, 2, 2, 7]
    >>> c  # c remains unchanged
    [3, 3, 2, 4, 1]
    >>> trade(a, c)  # Trades 4+3+1=8 for 3+3+2=8
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    >>> d = [1, 1]
    >>> e = [2]
    >>> trade(d, e)  # Trades 1+1=2 for 2=2
    'Deal!'
    >>> d
    [2]
    >>> e
    [1, 1]
    """
    m, n = 1, 1

    equal_prefix = lambda: sum(first[:m]) == sum(second[:n])
    while not equal_prefix() and (m<=len(first)) and (n<=len(second)):
        if sum(first[:m]) < sum(second[:n]):
            m += 1
        else:
            n += 1

    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'


def filter(condition, lst):
    """Filters lst with condition using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    i=0
    while i<len(lst):
        if not condition(lst[i]):
            del lst[i]
        else:
            i +=1

