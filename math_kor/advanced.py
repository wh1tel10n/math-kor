"""
복잡한 수학 공식을 한글로 풀 수 있습니다.
"""
def 최대공약수(a, b):
    """
    최대공약수를 반환하는 함수입니다. 
    >>> 최대공약수(18,30)
    6
    >>> 최대공약수(1.3, 19)
    Traceback (most recent call last):
        ...
    AssertionError: params should be an integer
    """
    assert type(a) is IntType, "params should be an integer"
    assert type(b) is IntType, "params should be an integer"
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a
