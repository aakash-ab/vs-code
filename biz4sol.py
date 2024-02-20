a train can travel at speed 50% faster than a car bith strt from tkinter import N
from point a at same time & reach
point b at same time & distance between a and b is 75km (12.5 minutes stoppage time lost for train) &
find speed of the car?


accept no from n. if no n > 0
create array of length of n square
create single dimension of array 4
square(3) = 0,0,1,0,2,1,3,2,1
square(4) = 0,0,0,1,0,0,2,1,0,3,2,1,4,3,2,1

n = 3
arr = [3] * n
print(arr)

rows,col = (3,3)
arr = [[0]*cols]*rows
arr[0][0]=1
for row in arr:
    print(row)
arr = [[3 for i in range(col)]for j in range(rows)]

for i in range(rows):
    col = []
    for j in range(col):
        col.append(0)
    arr.append(col)
print(arr)

str1 = 'india'
print('duplicates are')
for i in range(0, len(str1)):
    count = 1
    for j in range(i+1, len(str1)):
        if(str1[i] == str1[j] and str1[i]!=''):
            count = count + 1
            print(count)
            str1 = str1[:j] + '0' + str1[j+1]
        if(count > 1 and str1[i]!='0'):
            print(str1[i])


