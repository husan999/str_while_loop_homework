def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    i=0
    while i<len(s):
        
        if s[i].isdigit():
            a+=1
        i+=1
    return a
print(main("Pyt88hon2001"))