def el(s,i):
    c = ''
    d = list(s)
    d.pop(i)
    for i in d:
        c += i
    return c

