def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum=0
    i=0
    while i<len(s):
        if str(s[i]).isdigit():
            if int(s[i])%2==0:
                sum+=1
        i+=1
    return sum
print(main("56786543250"))