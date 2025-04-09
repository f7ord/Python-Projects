#TODO: tweak the program so it takes command line arguments
#TODO: make it work for higher bases like 16

def base_convert(num: int, b: int):
    """ Basic base conversion program
        num: the number to convert
        b: the base to convert the number to
        Return num in base b
    """
    ans = []
    while num:
        ans.insert(0, num % b)
        num = num // b
    return ''.join(str(i) for i in ans)


print(base_convert(int('1100', 2), 10))  # 12
print(base_convert(256, 2))  # 100000000
