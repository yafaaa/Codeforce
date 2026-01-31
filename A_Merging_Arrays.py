def main():
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pa, pb = 0, 0
    l = []
    while pa < x and pb < y:
        if a[pa] < b[pb]:
            l.append(a[pa])
            pa += 1
        else:
            l.append(b[pb])
            pb += 1
    while pa < x:
        l.append(a[pa])
        pa += 1
    while pb < y:
        l.append(b[pb])
        pb += 1
    print(*l)
if __name__ == "__main__":
    main()

