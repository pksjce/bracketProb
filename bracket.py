def brackets(n):
    return bracketsPrefix("", n, n)

def bracketsPrefix(prefix, opens, closes):
    total = 0
    assert opens<=closes
    if opens==0 and closes==0:
        total = 1
        print prefix
    if closes>opens:
        total += bracketsPrefix(prefix+")", opens, closes-1)
    if opens>0:
        total += bracketsPrefix(prefix+"(", opens-1, closes)
    return total

if __name__=="__main__":
    for i in range(6):
        n = brackets(i)
        print i,n
        x = raw_input("** ")
