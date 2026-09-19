def elec(a, b, c):

    cal1 = 0
    cal2 = 0
    cal3 = 0

    if a > b > c:

        cal2 = a - b + 1
        cal3 = a - c + 1

    elif a > c > b:

        cal3 = a - c + 1
        cal2 = a - b + 1

    elif b > a > c:

        cal1 = b - a + 1
        cal3 = b - c + 1

    elif b > c > a:

        cal3 = b - c + 1
        cal1 = b - a + 1

    elif c > a > b:

        cal1 = c - a + 1
        cal2 = c - b + 1

    elif c > b > a:

        cal2 = c - b + 1
        cal1 = c - a + 1

    elif a == b and a > c:

        cal1 = 1
        cal2 = 1
        cal3 = a - c + 1

    elif a == b and a < c:

        cal1 = c - a + 1
        cal2 = c - b + 1
        cal3 = 0

    elif a == c and a > b:

        cal1 = 1
        cal2 = a - b + 1
        cal3 = 1

    elif a == c and a < b:

        cal1 = b - a + 1
        cal2 = 0
        cal3 = b - c + 1

    elif b == c and b > a:

        cal1 = b - a + 1
        cal2 = 1
        cal3 = 1

    elif b == c and b < a:

        cal1 = 0
        cal2 = a - b + 1
        cal3 = a - c + 1

    else:

        cal1 = 1
        cal2 = 1
        cal3 = 1

    print(cal1, cal2, cal3)


n = int(input())

for i in range(1, n + 1):

    a, b, c = map(int, input().split())
    elec(a, b, c)