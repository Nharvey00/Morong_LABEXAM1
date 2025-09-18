def tower_hanoi(n, source, auxilliary, target):
    if n == 1:
        print("Move disk 1 from rod "+ source + " to rod "+ target)
        return
    tower_hanoi(n-1, source, target, auxilliary)
    print("Move disk "+str(n) + " from rod"+ source + " to rod "+ target)
    tower_hanoi(n-1, auxilliary, source, target)

num = int(input("Enter number: "))
tower_hanoi(num, "A", "B", "C")