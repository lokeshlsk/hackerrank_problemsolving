def aVeryBigSum(ar):
    res = 0
    for i in ar:
        res = res + i
    return res

ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
result = aVeryBigSum(ar)
print(result)
