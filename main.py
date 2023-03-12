# python3
# Aleksejs Šepeļevs, 221RDB494

def parallel_processing(n, m, data):
    output = []
    tests = []

    for i in range (n):
        tests.append(0)
    i = 0

    while i<m:
        laiks = tests[0]
        first = 0
        j = 1
        while j < n:
            if tests[j]<laiks:
                laiks=tests[j]
                first = j
            j = j + 1

        second = tests[first]
        tests[first] += data[i]
        output.append((first, second))
        i = i + 1
    return output

def main():
    n = 0
    m = 0
    data = []

    n, m = map(int, input().split())
    assert m >= 1
    assert m <= 105
    assert n >= 1
    assert n <= 105

    data = list(map(int, input().split()))
    assert len(data) == m

    for i in range(m):
        assert data[i] >= 0
        assert data[i] <= 110

    result = parallel_processing(n,m,data)
    for i in range(len(result)):
        print(result[i][0], result[i][1])
        
if __name__ == "__main__":
    main()
