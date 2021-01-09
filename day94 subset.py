for i in range (int(input())):
    c, a = input(), set(input().split())
    d, b = input(), set(input().split())
    print(b.intersection(a) == a)
