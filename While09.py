def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    i=0
    while i<len(s):
        if str(s[i]).isdigit():
                a+=int(s[i])
        i+=1
    return a
print(main("987654"))