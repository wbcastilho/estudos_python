def fizz_buzz(n: int):
    """
    >>> fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz

    :param n:
    :return:
    """
    for i in range(1, n+1):
        result = ""
        if i % 2 == 0:
            result = "fizz"
        if i % 3 == 0:
            result += "buzz"
        '''if result == "":
            result = i
        print(result)'''
        print(i if result == '' else result)


fizz_buzz(5)
