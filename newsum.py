op = ['-', '+']
num = ['1','2','3','4','5','6','7','8','9','-','0']
lett = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def newsum(a,b):
    a = list(a)
    b = list(b)
    q1 = ''
    w1 = ''
    q2 = ''
    w2 = ''
    i = 0
    while a[i] in num:
        q1+=a[i]
        a.pop(i)
        
    for i in a:
        w1+=i
    i = 0
    while b[i] in num:
        q2 += b[i]
        b.pop(i)
        
    for i in b:
        w2 += i
    if w1 == w2:
        return str(int(q1)+int(q2))+w1
    else:
        return "errore"

print(newsum("2a^2", '2a^2'))
