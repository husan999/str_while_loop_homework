def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0 
    i=0
    while i<len(s):
        if str(s[i]).isdigit():
            if int(s[i])%2==1:
                a+=1
            i+=1
    return a
print(main("1567534"))