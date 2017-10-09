n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print("%.5f" % (sum(i > 0 for i in arr) / n))
print("%.5f" % (sum(i < 0 for i in arr) / n))
print("%.5f" % (sum(i == 0 for i in arr) / n))