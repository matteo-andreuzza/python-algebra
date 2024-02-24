#? restituisce parte letterale di monomio
op = ['-', '+']
num = ['1','2','3','4','5','6','7','8','9', '-', '0']
lett = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def letpart(mon):
    mon = list(mon)
    q1 = ''
    w1 = ''
    i = 0
    while mon[i] in num:
        q1+=mon[i]
        mon.pop(i)
        
    for i in mon:
        w1+=i
    return w1

def numpart(mon):
    mon = list(mon)
    q1 = ''
    w1 = ''
    i = 0
    while mon[i] in num:
        q1+=mon[i]
        mon.pop(i)
        
    return q1

print(letpart("45avc"))
print(numpart("45av^2c"))