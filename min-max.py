#finding max/min in an array
n = int(input("Enter number of elements: "))
arr = []
for i in range (n):
    arr.append(int(input()))

max_val = arr[0]
min_val = arr[0]

for n in arr:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print("Maximum value:", max_val)
print("Minimum value:", min_val)