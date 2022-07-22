import sys

def calc_width(city, flights, widths):
    if widths[city][0] > -1:
        return widths[city][0]

    if len(flights[city]) == 1:
        widths[city] = 1 + calc_width()
        return

def longest_path(L, flights):
    L[n-1] = [n-1] # base case
    longest_path = L[n-1]
    for s in range(n-2, 0, -1): # recursive case
        L[s] = [s]
        for v in flights[s]:
            if len([s] + L[v]) > len(L[s]):
                L[s] = [s] + L[v]
        if len(L[s]) > len(longest_path):
            longest_path = L[s]
    return longest_path

sys.stdin = open("11695.txt")

cases = int(sys.stdin.readline())

for i in range(cases):
    n = int(sys.stdin.readline())

    flights = {}
    for j in range(n-1):
        m = sys.stdin.readline().strip().split()
        a,b = int(m[0]), int(m[1])

        if a not in flights:
            flights[a] = []
        if b not in flights:
            flights[b] = []

        flights[a].append(b)
        flights[b].append(a)

    widths = {}
    L = {}
    for j in flights:
        widths[j] = [-1, -1]
        L[j] = [j]

    e = longest_path(L, flights)
    print(e)
