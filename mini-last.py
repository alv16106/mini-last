f1 = lambda x, x2: (15 * x) + (30 * x2) + (4 * x * x2) - (2 * x ** 2) - (4 * x2 ** 2)

f2 = lambda x, x2: 3 * x + 5 * x2 

f3 = lambda x, x2: 5 * x - x ** 2 + 8 * x2 - 2 * x2 ** 2 

r1 = lambda x, x2: (x + 2 * x2) > 30

r2 = lambda x, x2: (3 * x + 2 * x2) > 18

r3 = lambda x, x2: (3 * x + 2 * x2) > 6

def getMax(f, limx, limx2, restriction):
    m = 0
    for x in range(0, limx):
        for x2 in range(0, limx2):
            if restriction(x, x2):
                continue
            m = max(m, f(x, x2))
    return m

if __name__ == "__main__":
    print(getMax(f1, 31, 16, r1))
    print(getMax(f2, 5, 7, r2))
    print(getMax(f3, 3, 4, r3))