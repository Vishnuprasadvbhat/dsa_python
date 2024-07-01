def int_to_str(n, b):
    string = '0123456789ABCDEF'
    if n < b:
        return string[n]

    return int_to_str(n//b, b) + string[n % b]





print(int_to_str (25852,16))