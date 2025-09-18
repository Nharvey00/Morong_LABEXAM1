def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)

def lcm(a,b):
    return a * b // gcf(a,b)

while True:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        print("Invalid integer ")
        continue
    x = a
    b = int(input("Enter a positive integer: "))
    if b <= 0:
        print("Invalid integer ")
        continue
    y = b
    break

print("The lcm of "+ str(a)+ " and "+ str(b) + " is "+ str(lcm(x,y)))
